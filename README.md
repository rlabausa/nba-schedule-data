# NBA-Schedule-Data
This repository contains tools, information, and documentation for accessing NBA season/post-season data that is available through `data.nba.com`. 

## Accessing the Schedule Data
The full JSON file for an NBA season schedule (_2015 or later_) can be accessed through the URL:
```
https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/{YEAR}/league/00_full_schedule.json

```
## JSON Structure
```
 + lscd
    + mscd
        + mon
        + g
            - gid
            - gcode
            - seri
            - is
            - gdte
            - htm
            - vtm
            - etm
            - an
            - as
            - st
            - stt
            + bd
                + b ...
            + v
                - tid
                - re
                - ta
                - tn
                - tc
                - s
            + h
                - tid
                - re
                - ta
                - tn
                - tc
                - s
            - gdtutc
            - utctm
            - ppdst
            + ptsls ...
    + mscd 
    + mscd
    ...
               
```


## JSON Breakdown

Name | Description | Value Type | Example
------------ | ------------ | ------------ | ------------ 
| `lscd` | League Schedule | _Array of JSON Objects_ | 
| `mscd` | Month Schedule | _Array of JSON Objects_ |
| `mon` | Month | _String_ | `"June"`
| `g` | Games | _Array of JSON Objects_ |
| `gid` | Game ID | _String_ | `"0041500407"`
| `gcode` | Game Code | _String_ | `"20160619/CLEGSW"`
| `seri` | Playoff Series Summary | _String_ | `"CLE wins series 4-3"`
| `gdte` | Game Date | _String_ | `"2016-06-19"`
| `an` | Arena | _String_ | `"ORACLE Arena"`
| `ac` | Arena City | _String_ | `"Oakland"`
| `as` | Arena State | _String_ | `"CA"`
| `stt` | Game Status | _String_ | `"Final"`
| `bd` | Broadcast Information | _JSON Object_ |
| `b` | Broadcasters | _Array of JSON Objects_ |
| `v` | Visiting Team Information | _JSON Object_ |
| `h` | Home Team Information | _JSON Object_ | 
| `tid` | Team ID | _Integer_ | `1610612739`
| `re` | W-L Record | _String_ | `"16-5"`
| `ta` | Team Abbreviation | _String_ | `"CLE"`
| `tn` | Team Name | _String_ | `"Cavaliers"`
| `tc` | Team City | _String_ | `"Cleveland"`
| `s` | Team Score | _String_ | `"93"`
| `gdtutc` | Game Date UTC | _String_ | `"2016-06-20"`
| `utctm` | UTC Time | _String_ | `"00:00"`

Examples for data collection can be found [here](https://github.com/rlabausa/nba-schedule-data/tree/master/python).






