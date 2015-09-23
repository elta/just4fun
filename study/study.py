#! /usr/bin/python
# vim: set fileencoding=utf-8 :

import time

head = [
        "BEGIN:VCALENDAR",
        "CALSCALE:GREGORIAN",
        "VERSION:2.0",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:学习",
        "X-WR-TIMEZONE:Asia/Harbin",
        "X-APPLE-CALENDAR-COLOR:#CC73E1",
        "BEGIN:VTIMEZONE",
        "TZID:Asia/Harbin",
        "BEGIN:STANDARD",
        "TZOFFSETFROM:+0900",
        "RRULE:FREQ=YEARLY;UNTIL=19910914T150000Z;BYMONTH=9;BYDAY=3SU",
        "DTSTART:19890917T000000",
        "TZNAME:GMT+8",
        "TZOFFSETTO:+0800",
        "END:STANDARD",
        "BEGIN:DAYLIGHT",
        "TZOFFSETFROM:+0800",
        "DTSTART:19910414T000000",
        "TZNAME:GMT+8",
        "TZOFFSETTO:+0900",
        "RDATE:19910414T000000",
        "END:DAYLIGHT",
        "END:VTIMEZONE",
        ]

tail = ["END:VCALENDAR",]

"""
useFormate = [
        "BEGIN:VEVENT",
        "CREATED:20150911T030614Z",
        "TRANSP:OPAQUE",
        "DTSTAMP:20150911T030614Z",
        "SEQUENCE:0",
        "SUMMARY:dddd",
        "DTSTART;TZID=Asia/Harbin:20150708T240000",
        "DTEND;TZID=Asia/Harbin:20150708T000000",
        "DESCRIPTION:dddfffxx",
        "END:VEVENT",
        ]
"""

def addDiary(start = "0", end = "0", tittle = "tittle", desc = "desc"):
    print "BEGIN:VEVENT"
    print "CREATED:20150911T030614Z"
    print "TRANSP:OPAQUE"
    print "DTSTAMP:20150911T030614Z"
    print "SEQUENCE:0"
    print "SUMMARY:" + tittle
    print "DTSTART;TZID=Asia/Harbin:" + start
    print "DTEND;TZID=Asia/Harbin:" + end
    print "DESCRIPTION:" + desc
    print "END:VEVENT"

"""
week
day : 6, 7
classtime: 0: beforenoon, 1 afternoon, 2 all day long
"""
def getTime(week = 0, day = 6, classtime = 2, classname = "class", classdesc = "101"):
    classtimeStr = [
            "T080000", "T120000",
            "T130000", "T170000",
            "T080000", "T170000"
            ]

    week_0 = "2015-8-31"
    timeArray = time.strptime(week_0, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))

    timeStamp = timeStamp + week * (7 * 24 * 60 * 60)
    timeStamp = timeStamp + (day - 1) * 24 * 60 * 60

    localtimeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y%m%d", localtimeArray)

    start = otherStyleTime + classtimeStr[classtime * 2]
    end   = otherStyleTime + classtimeStr[classtime * 2 + 1]

    addDiary(start, end, classname, classdesc)


all = [
        ["英语2-1班", "40/2", "1.2.6.7.8.9.10.11", "周六 上午", "304"],
        ["英语2-2班", "40/2", "1.2.6.7.8.9.10.11", "周六 上午", "305"],
        ["英语2-3班", "40/2", "1.2.6.7.8.9.10.11", "周六 上午", "315"],
        ["英语2-4班", "40/2", "1.2.6.7.8.9.10.11", "周六 上午", "316"],
        ["知识产权—管理", "20/1", "8.9.10.11", "周六 上午", "阶一5"],
        ["知识产权—IT", "20/1", "12.13.14.15", "周六 上午", "阶一6"],
        ["信息检索—IT", "20/1", "16.18.19.20", "周六 上午", "阶一6"],
        ["信息检索—管理", "20/1", "8.9.10.11", "周六 下午", "阶一5"],
        ["项目管理软件应用", "40/2", "1.2.6.7", "周六 全天", "机房"],
        ["高级管理学", "40/2", "12.13.14.15.16.18.19.20", "周日 上午", "阶一5"],
        ["工程论证与决策", "40/2", "1.2.6.7.8.9.10.11", "周六 上午", "Z408"],
        ["工程管理概论", "40/2", "1.2.6.7.8.9.10.11", "周六 下午", "Z408"],
        ["管理中的数学方法及应用", "40/2", "1.2.6.7.8.9.10.11", "周日 上午", "阶一5"],
        ["计算机辅助设计与制造", "40/2", "1.2.6.7.8.9.10.11", "周六 晚上", "Z404"],
        ["工业工程概论", "40/2", "12.13.14.15.16.18.19.20", "周日 下午", "Z404"],
        ["人因工程学", "40/2", "12.13.14.15.16.18.19.20", "周六 下午", "Z404"],
        ["质量管理", "40/2", "12.13.14.15.16.18.19.20", "周六 上午", "阶一1"],
        ["人力资源管理", "40/2", "12.13.14.15.16.18.19.20", "周六 上午", "阶二1"],
        ["财务与成本管理", "40/2", "12.13.14.15.16.18.19.20", "周日 下午", "阶一5"],
        ["项目组合管理", "40/2", "12.13.14.15.16.18.19.20", "周六 下午", "阶一1"],
        ["应急信息管理技术", "20/1", "1.2.6.7", "周日 下午", "阶二1"],
        ["软件体系结构", "40/2", "2.7.9.11", "周日 全天", "阶二5"],
        ["软件项目管理", "40/2", "1.6.8.10", "周日 全天", "阶二5"],
        ["软件测试与质量保证", "40/2", "1.2.6.7.8.9.10.11", "周六 下午", "阶二5"],
        ["数据挖掘", "40/2", "12.13.14.15.16.18.19.20", "周六 下午", "阶二5"],
        ["商业智能", "40/2", "12.13.14.15.16.18.19.20", "周日 下午", "阶一1"],
        ["非关系型数据库系统", "40/2", "12.13.14.15.16.18.19.20", "周日 上午", "阶一1"],
        ["计算机网络技术", "40/2", "1.2.6.7.8.9.10.11", "周日 上午", "阶一3"],
        ["无线网络技术", "40/2", "1.2.6.7.8.9.10.11", "周六 下午", "阶一1"],
        ["现代数据通信网", "40/2", "12.13.14.15", "周日 全天", "阶二2"],
        ["信息安全体系结构", "40/2", "12.13.14.15.16.18.19.20", "周日 上午", "阶一2"],
        ["计算机图形学", "40/2", "1.2.6.7.8.9.10.11", "周六 下午", "阶一2"],
        ["图形学技术实践", "20/1", "8.9.10.11", "周六 晚上", "阶一2"],
        ["3D仿真/游戏引擎技术原理与实践", "40/2", "12.13.14.15.16.18.19.20", "周六 下午", "阶一2"],
        ["实时嵌入式操作系统", "40/2", "1.2.6.7.8.9.10.11", "周六 下午", "阶二1"],
        ["数字图像处理", "40/2", "1.2.6.7.8.9.10.11", "周日 上午", "阶一2"],
        ["EDA工具原理与应用", "40/2", "1.2.6.7.8.9.10.11", "周六 晚上", "阶二1"],
        ["大数据技术概论", "40/2", "1.2.6.7.8.9.10.11", "周日 下午", "阶一1"],
        ["集成数据管理", "40/2", "16.18.19.20", "周日 全天", "阶二4"],
        ["专利信息检索与利用", "20/1", "8.9.10.11", "周日 下午", "阶二1"],
        ["专利代理实务与技巧", "20/1", "12.13.14.15", "周六 下午", "阶一3"],
        ["职业生涯管理", "20/1", "8.9", "周日下午+晚上", "阶一5"],
        ["创新管理学", "20/1", "16.18.19.20", "周日 下午", "阶二5"],
        ["金融IT治理及风险管理 ", "30/1.5", "12.13.14.15.16.18", "周六 下午", "阶二1"],
        ["金融支付概论/第三方支付 ", "30/1.5", "6.7.8.9.10.11", "周日 下午", "阶一2"],
        ["云计算中的并行SOA及大数据应用开发基础：Platform Symphony ", "20/1", "1,2", "周日 全天", "阶一4"],
        ["大数据与Spark", "20/1", "9.10", "周日 全天", "阶一4"],
      ];

class_name = []

for i in all:
    class_name.append(i[0])

my_class = [
    "高级管理学",
    "软件体系结构",
    "软件项目管理",
    "实时嵌入式操作系统",
    "项目组合管理",
    "商业智能",
    "英语2-3班",
    "知识产权—IT",
    "信息检索—IT",
    ]

class_time = [
        "周六",
        "周日",
        "上午",
        "下午",
        "全天",
    ]

week = range(0, 88)
#print week

for item in head:
    print item

for myStudy in my_class:
    index = class_name.index(myStudy)
    #print "========="
    #print class_name[index]
    onClassTime = all[index][3]

    for u_week in all[index][2].split("."):
        week_num = int(u_week) * 4
        # 周六
        if onClassTime.__contains__(class_time[0]):
            # beforenoon
            if onClassTime.__contains__(class_time[2]):
                week[week_num] = class_name[index]
                getTime(week_num/4, 6, 0, class_name[index], class_name[index] + ":" + all[index][4])
            if onClassTime.__contains__(class_time[3]):
                # afternoon
                week[week_num + 1] = class_name[index]
                getTime(week_num/4, 6, 1, class_name[index], class_name[index] + ":" + all[index][4])
            if onClassTime.__contains__(class_time[4]):
                # All days long
                week[week_num] = class_name[index]
                week[week_num + 1] = class_name[index]
                getTime(week_num/4, 6, 2, class_name[index], class_name[index] + ":" + all[index][4])
        # 周日
        if onClassTime.__contains__(class_time[1]):
            # beforenoon
            if onClassTime.__contains__(class_time[2]):
                week[week_num + 2] = class_name[index]
                getTime(week_num/4, 7, 0, class_name[index], class_name[index] + ":" + all[index][4])
            # afternoon
            if onClassTime.__contains__(class_time[3]):
                week[week_num + 3] = class_name[index]
                getTime(week_num/4, 7, 1, class_name[index], class_name[index] + ":" + all[index][4])
            if onClassTime.__contains__(class_time[4]):
                # All days long
                week[week_num + 2] = class_name[index]
                week[week_num + 3] = class_name[index]
                getTime(week_num/4, 7, 2, class_name[index], class_name[index] + ":" + all[index][4])

for item in tail:
    print item

