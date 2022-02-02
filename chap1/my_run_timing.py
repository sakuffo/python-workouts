def run_timing():
    total_run_time = 0
    total_runs = 0
    while True:
        try:
            run_time = input("Enter 10 km run time: ")
            if not run_time:
                if not total_runs:
                    break
                else:
                    avg_time = total_run_time/total_runs
                    print(f'\nAverage of {avg_time}, over {total_runs} runs')
                    break

            if run_time:
                total_run_time += float(run_time)
                total_runs += 1
        except ValueError as e:
            print("Hey! That\'s not a valid number!")


run_timing()
