def is_available(candidate, current_col):
    # how to get current_row
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def dfs(num, current_row, current_candidate, final_result):
    if current_row == num:
        final_result.append(current_candidate[:])
        return
    for candidate_col in range(num):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(num, current_row + 1, current_candidate, final_result)
            # back track
            current_candidate.pop()


def solve_n_queens(num):
    final_result = []
    dfs(num, 0, [], final_result)
    return final_result


if __name__ == "__main__":
    print(solve_n_queens(4))
