# usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import abc
import dataclasses
import random
import sys
import time
from typing import Final

random.seed(0)  # 調査のためシード値を固定しておく


@dataclasses.dataclass
class Environment:  # 問題環境
    span: Final[int]
    num_contests: Final[int]
    params_c: Final[dict[int, int]]  # 満足度減少パラメーター
    params_s: Final[dict[tuple[int, int], int]]  # 満足度増加パラメーター


class Evaluator:  # スケジュール評価機能
    def __init__(self, env: Environment) -> None:
        self.env = env

    def evaluate(self, schedule: Schedule) -> int:
        last_dates = {i: 0 for i in range(1, self.env.num_contests + 1)}
        total_satisfaction = 0
        for d in range(1, self.env.span + 1):
            hold_contest_id = schedule[d]
            # 最後のコンテスト開催日を更新する
            last_dates[hold_contest_id] = d
            # 開かれなかったコンテストによる満足度の低下を計算する
            for i in range(1, self.env.num_contests + 1):
                total_satisfaction -= (d - last_dates[i]) * self.env.params_c[i]
            # 開かれたコンテストによる満足度の増加を足す
            total_satisfaction += self.env.params_s[d, hold_contest_id]
        return total_satisfaction


class Schedule:
    def __init__(self, env: Environment) -> None:
        self.env = env
        self.evaluator = Evaluator(env)
        self.schedule: dict[int, int] = {}
        self.satisfaction: int = 0
        # 貪欲法によるスケジュールを求めておく
        self.generate_greedy_schedule()
        self.evaluate()

    def __getitem__(self, date: int) -> int:
        return self.schedule[date]

    def print_schedule(self) -> None:
        for d in range(1, self.env.span + 1):
            print(self.schedule[d])

    def evaluate(self) -> None:
        self.satisfaction = self.evaluator.evaluate(self)

    def get_satisfaction(self) -> int:
        self.evaluate()
        return self.satisfaction

    def overwrite(self, date: int, contest: int) -> None:
        self.schedule[date] = contest

    def generate_greedy_schedule(self) -> None:  # 貪欲法によるスケジュール生成
        last_dates = {i: 0 for i in range(1, self.env.num_contests + 1)}
        for d in range(1, self.env.span + 1):
            max_satisfaction = -1 * sys.maxsize
            best_contest_id = 1
            for i in range(1, self.env.num_contests + 1):
                old_last_date = last_dates[i]
                last_dates[i] = d
                scr = self.env.params_s[d, i]
                scr -= sum(self.env.params_c[j] * (d - last_dates[j]) for j in range(1, self.env.num_contests + 1))
                if max_satisfaction < scr:
                    max_satisfaction = scr
                    best_contest_id = i
                last_dates[i] = old_last_date
            last_dates[best_contest_id] = d
            self.schedule[d] = best_contest_id


class Neighborhood(metaclass=abc.ABCMeta):
    def __init__(self, env: Environment) -> None:
        self.env = env
        self.schedule: Schedule

    def set_schedule(self, schedule: Schedule) -> None:
        self.schedule = schedule

    @abc.abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError()

    def get_satisfaction(self) -> int:
        return self.schedule.get_satisfaction()


class SingleContestExchanger(Neighborhood):
    def __init__(self, env: Environment) -> None:
        super().__init__(env)
        self.decided_date: int
        self.decided_contest: int
        self.original_contest: int

    def execute(self) -> None:
        self.decided_date = random.randint(1, self.env.span)
        self.decided_contest = random.randint(1, self.env.num_contests)
        self.original_contest = self.schedule[self.decided_date]
        self.schedule.overwrite(self.decided_date, self.decided_contest)

    def rollback(self) -> None:
        self.schedule.overwrite(self.decided_date, self.original_contest)


def hill_climbing(env: Environment, schedule: Schedule) -> Schedule:
    TIME_LIMIT = 1.8

    cnt: int = 1
    start_time = time.perf_counter()
    calculation_time = 0.0
    best_schedule: Schedule = schedule
    best_satisfaction: int = schedule.get_satisfaction()
    neighbor = SingleContestExchanger(env)  # 近傍の生成方法を固定
    while True:
        if cnt % 30 == 0:
            calculation_time = time.perf_counter() - start_time
        if calculation_time > TIME_LIMIT:
            break
        neighbor.set_schedule(best_schedule)
        neighbor.execute()  # 近傍解生成
        satisfaction = neighbor.get_satisfaction()
        if satisfaction > best_satisfaction:  # 近傍解が元の解より良ければ受容する
            best_satisfaction = satisfaction
            best_schedule = neighbor.schedule
        else:
            neighbor.rollback()  # 近傍解が悪い場合は元のスケジュールに戻す
        cnt += 1
    return best_schedule


def main():
    SPAN = int(input())  # スケジュール生成期間
    num_contests = 26  # コンテストは A から Z まで 26個存在する

    # c: 満足度低下パラメータ の受け取り
    params_c: dict[int, int] = {}
    for i, x in enumerate(sys.stdin.readline().rstrip().split(), 1):
        params_c[i] = int(x)

    # s: 満足度増加パラメータ の受け取り
    params_s: dict[tuple[int, int], int] = {}
    for d in range(1, SPAN + 1):
        for i, x in enumerate(sys.stdin.readline().rstrip().split(), 1):
            params_s[d, i] = int(x)

    env = Environment(SPAN, num_contests, params_c, params_s)  # 問題環境の構築
    init_schedule = Schedule(env)  # 初期スケジュール生成
    best_schedule = hill_climbing(env, init_schedule)  # 山登り法による探索
    best_schedule.print_schedule()  # スケジュール表示


if __name__ == "__main__":
    main()
