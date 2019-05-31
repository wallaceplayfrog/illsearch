from django.shortcuts import render
from .models import Info, Complain, Diagnose, Dispose
import jieba
from jieba import analyse
import os


# Create your views here.


def main(request):

    return render(request, 'main.html', {"title": "病例查询系统"})


def personal(request):

    rec_text = request.GET.get('name')
    rec_num = request.GET.get('num')
    post_list = Info.objects.filter(name=rec_text, num=rec_num)

    if not post_list:
        error_msg = "未找到" + rec_text + "的资料"
        return render(request, 'personal.html', {"title": "查询结果",
                                                 "error_msg": error_msg})
    else:
        num = post_list[0].num

        man_complain = Complain.objects.filter(num=num)
        man_complain_list = []
        if man_complain[0].word1 != "":
            man_complain_list.append(man_complain[0].word1)
        if man_complain[0].word2 != "":
            man_complain_list.append(man_complain[0].word2)
        if man_complain[0].word3 != "":
            man_complain_list.append(man_complain[0].word3)

        man_diagnose = Diagnose.objects.filter(num=num)
        man_diagnose_list = []
        if man_diagnose[0].ill1 != "":
            man_diagnose_list.append(man_diagnose[0].ill1)
        if man_diagnose[0].ill2 != "":
            man_diagnose_list.append(man_diagnose[0].ill2)
        if man_diagnose[0].ill3 != "":
            man_diagnose_list.append(man_diagnose[0].ill3)
        if man_diagnose[0].ill4 != "":
            man_diagnose_list.append(man_diagnose[0].ill4)
        if man_diagnose[0].ill5 != "":
            man_diagnose_list.append(man_diagnose[0].ill5)

        man_dispose = Dispose.objects.filter(num=num)
        man_dispose_list = []
        if man_dispose[0].med1 != "":
            man_dispose_list.append(man_dispose[0].med1)
        if man_dispose[0].med2 != "":
            man_dispose_list.append(man_dispose[0].med2)
        if man_dispose[0].med3 != "":
            man_dispose_list.append(man_dispose[0].med3)
        if man_dispose[0].med4 != "":
            man_dispose_list.append(man_dispose[0].med4)
        if man_dispose[0].med5 != "":
            man_dispose_list.append(man_dispose[0].med5)
        if man_dispose[0].med6 != "":
            man_dispose_list.append(man_dispose[0].med6)

        return render(request, 'personal.html', {"title": "查询结果",
                                                 "man_info": post_list,
                                                 "man_complain": man_complain_list,
                                                 "man_diagnose": man_diagnose_list,
                                                 "man_dispose": man_dispose_list,
                                                 })


def probability(request):

    text = request.GET.get('text')
    path = os.path.abspath('dict.txt')
    jieba.load_userdict(path)
    jieba.suggest_freq(('月', '余'), True)
    tfidf = analyse.extract_tags
    result_cpl = tfidf(text, allowPOS="n", topK=3)

    post_list = []
    if len(result_cpl) == 1:
        post_list1 = Complain.objects.filter(word1=result_cpl[0])
        for post in post_list1:
            post_list.append(post)
        post_list2 = Complain.objects.filter(word2=result_cpl[0])
        for post in post_list2:
            post_list.append(post)
        post_list3 = Complain.objects.filter(word3=result_cpl[0])
        for post in post_list3:
            post_list.append(post)
    if len(result_cpl) == 2:
        post_list1 = Complain.objects.filter(word1=result_cpl[0])
        for post in post_list1:
            post_list.append(post)
        post_list2 = Complain.objects.filter(word2=result_cpl[0])
        for post in post_list2:
            post_list.append(post)
        post_list3 = Complain.objects.filter(word3=result_cpl[0])
        for post in post_list3:
            post_list.append(post)
        post_list4 = Complain.objects.filter(word1=result_cpl[1])
        for post in post_list4:
            post_list.append(post)
        post_list5 = Complain.objects.filter(word2=result_cpl[1])
        for post in post_list5:
            post_list.append(post)
        post_list6 = Complain.objects.filter(word3=result_cpl[1])
        for post in post_list6:
            post_list.append(post)
    if len(result_cpl) == 3:
        post_list1 = Complain.objects.filter(word1=result_cpl[0])
        for post in post_list1:
            post_list.append(post)
        post_list2 = Complain.objects.filter(word2=result_cpl[0])
        for post in post_list2:
            post_list.append(post)
        post_list3 = Complain.objects.filter(word3=result_cpl[0])
        for post in post_list3:
            post_list.append(post)
        post_list4 = Complain.objects.filter(word1=result_cpl[1])
        for post in post_list4:
            post_list.append(post)
        post_list5 = Complain.objects.filter(word2=result_cpl[1])
        for post in post_list5:
            post_list.append(post)
        post_list6 = Complain.objects.filter(word3=result_cpl[1])
        for post in post_list6:
            post_list.append(post)
        post_list7 = Complain.objects.filter(word1=result_cpl[2])
        for post in post_list7:
            post_list.append(post)
        post_list8 = Complain.objects.filter(word2=result_cpl[2])
        for post in post_list8:
            post_list.append(post)
        post_list9 = Complain.objects.filter(word3=result_cpl[2])
        for post in post_list9:
            post_list.append(post)

    post_list = list(set(post_list))

    if not post_list:
        error_msg = "未找到" + text + "的资料"
        return render(request, 'probability.html', {"title": "查询结果",
                                                    "error_msg": error_msg})
    complain_list = []
    for post in post_list:
        man_complain_list = []
        if post.word1 != "":
            man_complain_list.append(post.word1)
        if post.word2 != "":
            man_complain_list.append(post.word2)
        if post.word3 != "":
            man_complain_list.append(post.word3)
        complain_list.append(man_complain_list)

    all_ill_list = []
    for post in post_list:
        man_diagnose = Diagnose.objects.filter(num=post.num)
        if man_diagnose[0].ill1 != "":
            all_ill_list.append(man_diagnose[0].ill1)
        if man_diagnose[0].ill2 != "":
            all_ill_list.append(man_diagnose[0].ill2)
        if man_diagnose[0].ill3 != "":
            all_ill_list.append(man_diagnose[0].ill3)
        if man_diagnose[0].ill4 != "":
            all_ill_list.append(man_diagnose[0].ill4)
        if man_diagnose[0].ill5 != "":
            all_ill_list.append(man_diagnose[0].ill5)
    all_ill_list = list(set(all_ill_list))

    ill_num_list = []
    for ill in all_ill_list:
        ill1_num = Diagnose.objects.filter(ill1=ill).count()
        ill2_num = Diagnose.objects.filter(ill2=ill).count()
        ill3_num = Diagnose.objects.filter(ill3=ill).count()
        ill4_num = Diagnose.objects.filter(ill4=ill).count()
        ill5_num = Diagnose.objects.filter(ill5=ill).count()
        ill_num = ill1_num + ill2_num + ill3_num + ill4_num + ill5_num
        ill_num_list.append(ill_num)

    ill_sum = 0
    for num in ill_num_list:
        ill_sum += num
    ill_probability_list = []
    for pro in ill_num_list:
        ill_probability_list.append(pro/ill_sum)

    cir_num = 0
    info_list = []
    while True:
        info_list.append([all_ill_list[cir_num], ill_num_list[cir_num], ill_probability_list[cir_num]])
        cir_num += 1
        if cir_num >= len(all_ill_list):
            break

    return render(request, 'probability.html', {"title": "得病概率",
                                                "man_complain": text,
                                                "all_info": info_list
                                                })


def way(request):

    text = request.GET.get('text')
    per = []
    per_ill1 = Diagnose.objects.filter(ill1=text)
    for tem in per_ill1:
        per.append(tem.num)
    per_ill2 = Diagnose.objects.filter(ill2=text)
    for tem in per_ill2:
        per.append(tem.num)
    per_ill3 = Diagnose.objects.filter(ill3=text)
    for tem in per_ill3:
        per.append(tem.num)
    per_ill4 = Diagnose.objects.filter(ill4=text)
    for tem in per_ill4:
        per.append(tem.num)
    per_ill5 = Diagnose.objects.filter(ill5=text)
    for tem in per_ill5:
        per.append(tem.num)
    per = list(set(per))

    example = dia_list = dis_list = []
    for num in per:
        man_diagnose = Diagnose.objects.filter(num=num)
        for tem in man_diagnose:
            dia_list = [tem.ill1, tem.ill2, tem.ill3, tem.ill4, tem.ill5]

        man_dispose = Dispose.objects.filter(num=num)
        for tem in man_dispose:
            dis_list = [tem.med1, tem.med2, tem.med3, tem.med4, tem.med5, tem.med6]
        example.append([dia_list, dis_list])
    return render(request, 'way.html', {"title": "解决办法",
                                        "his_info": example})