# usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import sys


class DecreaseParams:  # 満足度減少パラメータ
    def __init__(self) -> None:
        self.__params: dict[int, int] = {}

    def set_params(self) -> None:
        for i, x in enumerate(sys.stdin.readline().rstrip().split(), 1):
            self.__params[i] = int(x)

    def get(self, contest_id: int) -> int:
        return self.__params[contest_id]


class IncreaseParams:  # 満足度増加パラメータ
    def __init__(self, span: int) -> None:
        self.__span = span
        self.__params: dict[tuple[int, int], int] = {}

    def set_params(self) -> None:
        for d in range(1, self.__span + 1):
            for i, x in enumerate(sys.stdin.readline().rstrip().split(), 1):
                self.__params[d, i] = int(x)

    def get(self, date: int, contest_id: int) -> int:
        return self.__params[date, contest_id]


class Environment:  # 問題環境
    def __init__(self, span: int, num_contests: int) -> None:
        self.__span = span
        self.__num_contests = num_contests
        self.__c = DecreaseParams()
        self.__s = IncreaseParams(span)

    def get_span(self) -> int:
        return self.__span

    def get_num_contests(self) -> int:
        return self.__num_contests

    def set_decrease_params(self) -> None:
        self.__c.set_params()

    def set_increase_params(self) -> None:
        self.__s.set_params()

    def get_decrease_params(self) -> DecreaseParams:
        return self.__c

    def get_increase_params(self) -> IncreaseParams:
        return self.__s


class InitScheduleGenerator:  # 初期スケジュール生成機能
    def __init__(self, env: Environment) -> None:
        self.span = env.get_span()
        self.num_contests = env.get_num_contests()
        self.decrease_params = env.get_decrease_params()
        self.increase_params = env.get_increase_params()

    def get_greedy_schedule(self) -> dict[int, int]:
        schedule = {}
        last_dates = {i: 0 for i in range(1, self.num_contests + 1)}
        for d in range(1, self.span + 1):
            max_satisfaction = -1 * sys.maxsize
            best_contest_id = 1
            for i in range(1, self.num_contests + 1):
                old_last_date = last_dates[i]
                last_dates[i] = d
                scr = self.increase_params.get(d, i)
                scr -= sum(self.decrease_params.get(c) * (d - last_dates[c]) for c in range(1, self.num_contests + 1))
                if max_satisfaction < scr:
                    max_satisfaction = scr
                    best_contest_id = i
                last_dates[i] = old_last_date
            last_dates[best_contest_id] = d
            schedule[d] = best_contest_id
        return schedule


# [TODO] 差分計算をして高速化したい
class Evaluator:  # スケジュール評価機能
    def __init__(self, env: Environment) -> None:
        self.num_contests = env.get_num_contests()
        self.decrease_params = env.get_decrease_params()
        self.increase_params = env.get_increase_params()

    def calculate_satisfaction(self, schedule: dict[int, int]) -> int:
        last_dates = {i: 0 for i in range(1, self.num_contests + 1)}
        total_satisfaction = 0
        for d in range(1, len(schedule) + 1):
            score = 0
            hold_contest_id = schedule[d]
            # 最後のコンテスト開催日を更新する
            last_dates[hold_contest_id] = d
            # 開かれなかったコンテストによる満足度の低下を計算する
            for i in range(1, self.num_contests + 1):
                score -= (d - last_dates[i]) * self.decrease_params.get(i)
            # 開かれたコンテストによる満足度の増加を足す
            score += self.increase_params.get(d, hold_contest_id)
            total_satisfaction += score
        return total_satisfaction


def main():
    D = int(input())  # スケジュール生成期間
    num_contests = 26  # コンテストは A から Z まで 26個存在する

    env = Environment(D, num_contests)  # 問題環境の構築
    env.set_decrease_params()  # c: 満足度低下パラメータ の受け取り
    env.set_increase_params()  # s: 満足度増加パラメータ の受け取り

    evaluator = Evaluator(env)  # スケジュール評価機能の生成

    init_schedule_generator = InitScheduleGenerator(env)  # 初期スケジュール生成機能の生成
    schedule = init_schedule_generator.get_greedy_schedule()  # 初期スケジュール生成
    evaluator.calculate_satisfaction(schedule)  # スケジュール評価

    # スケジュール表示
    for d in range(1, D + 1):
        print(schedule[d])


if __name__ == "__main__":
    main()
