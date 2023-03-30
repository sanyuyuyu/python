#每月还款额=贷款本金*[月利率*(1+月利率) ^ 还款月数]%{[(1+ 月利率) ^ 还款月数]-11}


loan_type = input('请选择贷款类型:1.商业贷款 2.公积金贷款 3.组合贷款\n')
if loan_type != '3':
    loan_amount = float(input('请输入贷款金额(万)\n'))
    term = int(input('请选择期限(年):5、10、15、20、25\n'))
    if term in [5,10,15,20,25]:
        if term == 5:
            mon_rate = 0.045/12
            mon_pay = loan_amount * 10000 * (mon_rate * ((1 + mon_rate) ** (term * 12))) / (((1 + mon_rate) ** (term * 12 )) - 1)
            all_pay = mon_pay * term * 12
            interest = all_pay - loan_amount * 10000
            print('每月月供参考(元):{:.2f}元'.format(mon_pay))
            print('支付利息(元)：{:.2f}元'.format(interest))
            print('还款总额(元)：{:.2f}元'.format((all_pay)))
        else:
            if loan_type == '1':
                mon_rate = (4.90 / 100) / 12
                mon_pay = loan_amount * 10000 * (mon_rate * ((1 + mon_rate) ** (term * 12))) / (
                        ((1 + mon_rate) ** (term * 12)) - 1)
                all_pay = mon_pay * term * 12
                interest = all_pay - loan_amount * 10000
                print("每月月供参考（元）：{:.2f}元".format(mon_pay))
                print("支付利息（元）：{:.2f}元".format(interest))
                print("还款总额（元）：{:.2f}元".format(all_pay))

            elif loan_type == '2':
                if term == 5:
                    mon_rate = 0.0275 / 12
                else:
                    mon_rate =  0.0325 / 12
                    mon_pay = loan_amount * 10000 * (mon_rate * ((1 + mon_rate) ** (term * 12))) / (((1 + mon_rate) ** (term * 12)) - 1)
                all_pay = mon_pay * term * 12
                interest = all_pay - loan_amount * 10000
                print('每月月供参考(元):{:.2f}元'.format(mon_pay))
                print('支付利息(元)：{:.2f}元'.format(interest))
                print('还款总额(元)：{:.2f}元'.format((all_pay)))
            else:
                print('请输入合法的期限')
    else:
        business_loan = float(input('请输入商业贷款金额'))
        fund_loan = float(input('请输入公积金贷款金额(万):\n'))
        term = int(input('请选择期限(年):5、10、15、20、25\n'))
        if term in [5, 10, 15, 20, 25]:
            if term == 5:
                business_mon_rate = (4.75 / 100) / 12
                found_mon_rate = (2.75 / 100) / 12






























































