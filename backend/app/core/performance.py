import pm4py
from pm4py.algo.performance import algorithm as perf

def analyze_performance(event_log):
    result = perf.apply(event_log)
    return {
        "bottlenecks": [
            {"activity": str(k), "avg_time_h": float(v)}
            for k, v in result.items()
        ]
    }
