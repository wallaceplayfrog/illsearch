import re
import json
import jieba

p1 = '"words": ".+"'
pattern = re.compile(p1)

def get_current_string(alist, pattern):
    strings = ''
    while True:
        tempstr = alist.pop(0)
        if(re.match(pattern, tempstr)) is None:
            strings += tempstr
        else:
            alist.insert(0, tempstr)
            break
    return strings

def get_current_strings(alist, pattern):
    strings = ''
    while True:
        tempstr = alist.pop(0)
        if(re.match(pattern, tempstr)) is None:
            strings += ',' + tempstr
        else:
            alist.insert(0, tempstr)
            break
    return strings

def creat_info(num):
    alist = []
    with open('./已裁剪病历/json/bingli ({}).json'.format(str(num)), 'r') as fp:
        for item in pattern.findall(fp.read()):
            if item.strip('"words": "').strip('许永攀,手签答') is not '':
                alist.append(item.strip('"words": "').strip('许永攀,手签答'))

    info = {} #暂定为字典存储，KEY-VALUE

    basic = alist.pop(0).split(',') # 病人基本信息
    info['姓名'] = basic.pop(0)[3:]
    info['性别'] = basic.pop(0)[3:]
    info['年龄'] = basic.pop(0)[3:]
    info['科别'] = basic.pop(0)[3:]

    caretime = alist.pop(0) # 就诊时间
    info['就诊时间'] = caretime[5:]

    chief_complaint = alist.pop(0) # 病人主诉
    info['病人主诉'] = chief_complaint[5:]

    history_of_present_illness = get_current_string(alist, '舌诊.*') # 现病史
    info['现病史'] = history_of_present_illness[4:]

    tongue = alist.pop(0) # 舌诊
    info['舌诊'] = tongue[3:]

    pulse_taking = alist.pop(0) # 脉诊
    info['脉诊'] = pulse_taking[3:]

    past_medical_history = alist.pop(0) #既往病史
    info['既往史'] = past_medical_history[4:]

    physical_examination = get_current_string(alist, '辅助检查.*') # 体格检查
    info['体格检查'] = physical_examination.strip('体格检查:')

    assistant_examination = get_current_string(alist, '诊断.*') # 辅助检查
    info['辅助检查'] = assistant_examination.strip('辅助检查:')

    diagnose = get_current_strings(alist, '处理.*') # 诊断
    diagnose_l = diagnose.strip(',诊断:').split(',')
    info['诊断'] = diagnose_l

    treat = alist # 处理
    treat.pop(0)
    info['处理'] = treat

    with open('./已裁剪病历/struct/bingli ({}).json'.format(str(num)), 'w', encoding = 'utf-8') as fp:
        fp.write(json.dumps(info, ensure_ascii = False, indent = 4))

if __name__ == '__main__':
    for i in range(1, 100):
        creat_info(i)
