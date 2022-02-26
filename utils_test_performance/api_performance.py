import requests
import time
from chart_utils import draw_column_chart

API_HOST = "http://127.0.0.1:8000"
CHART_TIME_VALUES = []


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executed {func.__name__} in {round(end_time - start_time, 2)} seconds")
        print(f"Downloaded data of {len(result.json())} books")
        print(20 * '-')

        # Append the measured time to display it later on in the chart
        global CHART_TIME_VALUES
        CHART_TIME_VALUES.append(round(end_time - start_time, 2))

        return result

    return wrapper


@measure_execution_time
def call_slow_endpoint():
    return requests.get(API_HOST + "/books/slow/")


@measure_execution_time
def call_optimized_endpoint():
    return requests.get(API_HOST + "/books/optimized/")


if __name__ == "__main__":
    call_slow_endpoint()
    call_optimized_endpoint()

    draw_column_chart(("slow", "optimized"), CHART_TIME_VALUES)
