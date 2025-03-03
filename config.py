# these variables should be updated!!!
USER = "ALL" # username as below or "ALL" if everybody should be seen
UPDATE_INTERVAL = 30000 # in millisecond

# these variables should not be updated
TODO_DASHBOARD = "https://dashboards.sero.wh.rnd.internal.ericsson.com/epg_st_passrates/epg_st_passrates_weekly_master_to_do_team.html"
OUT_OF_DATE_DASHBOARD = "https://dashboards.sero.wh.rnd.internal.ericsson.com/epg_st_passrates/epg_st_passrates_weekly_master_not_run_team.html"
TCS = {
    "TC37512.4.6.1.53": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37540.1.6.11": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37540.40.6.1": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.4.6.1.53.1": {"scope": "Dynamic", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37485.1.6.1": {"scope": "2Extended", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "MAINTAINABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.4.6.10.1": {"scope": "2Extended", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37515.8.1.5.1": {"scope": "Basic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_BASIC", "Label4": "ST_DAILY", "Original Estimate": 86400, "Story Points": 3},
    "TC37512.4.4.18.23": {"scope": "Basic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_BASIC", "Label4": "ST_DAILY", "Original Estimate": 86400, "Story Points": 3},
    "TC37512.4.6.10.11": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.4.6.17.1": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.6.6.17.5": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.6.6.17.12": {"scope": "Dynamic", "owner": "ECSIGER", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC2020.5.6.9.5": {"scope": "2Extended", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC2020.5.6.14.1": {"scope": "Dynamic", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC1123.1.6.1.1": {"scope": "Dynamic", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC22687.1.1.2.1": {"scope": "Dynamic", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC22711.2.2.2.1": {"scope": "Extended", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37553.1.6.8": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37512.6.6.11.25": {"scope": "2Dynamic", "owner": "ETOTIST", "Label1": "REGRESSION", "Label2": "CAPACITY", "Label3": "ST_2DYNAMIC", "Label4": "ST_BI-MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37540.1.6.16": {"scope": "2Extended", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_2EXTENDED", "Label4": "ST_BI-WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC1122.1.1.10.1": {"scope": "Extended", "owner": "ETHNYZ", "Label1": "REGRESSION", "Label2": "ROBUSTNESS", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.3.6.1": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.3.6.2": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.3.6.3": {"scope": "Extended", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_EXTENDED", "Label4": "ST_WEEKLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.5.6.1": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.5.6.2": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.6.6.1": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5},
    "TC37548.6.6.2": {"scope": "Dynamic", "owner": "ERKMIAP", "Label1": "REGRESSION", "Label2": "STABILITY", "Label3": "ST_DYNAMIC", "Label4": "ST_MONTHLY", "Original Estimate": 14400, "Story Points": 0.5}
}
