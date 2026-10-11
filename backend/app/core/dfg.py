import pm4py
import pandas as pd
from pm4py.objects.conversion.log import converter

def dataframe_to_event_log(df: pd.DataFrame):
    df = df.rename(columns={
        "case_id": "case:concept:name",
        "activity": "concept:name",
        "timestamp": "time:timestamp",
    })
    df["time:timestamp"] = pd.to_datetime(df["time:timestamp"])
    return converter.apply(df, variant=converter.Variants.TO_EVENT_LOG)

def discover_dfg(event_log):
    dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
    return {
        "dfg": {f"{a}->{b}": c for (a, b), c in dfg.items()},
        "start": dict(start_activities),
        "end": dict(end_activities),
    }

def get_variants(event_log):
    variants = pm4py.get_variants(event_log)
    return [
        {"path": " -> ".join(variant), "count": count}
        for variant, count in variants.items()
    ]
