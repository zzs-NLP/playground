package com.example.atmdemo.service;

import com.example.atmdemo.entity.Account;
import com.example.atmdemo.entity.Bank;
import com.example.atmdemo.utils.R;

import java.util.HashMap;
import java.util.Random;


public class CustomerService {

    AccountService accountService = new AccountService();
    Bank bank = Bank.getInstance();
    //用户登录
    public R loginAccount(String code, Account account) {
        int cardId = account.getCardId();
        //单例模式
        Bank bank = Bank.getInstance();
        //从银行获取卡密码
        HashMap<Integer, String> cardsCode = bank.getCardsCode();
        String cardCode = cardsCode.get(cardId);
        //校验卡密码
        if (code.equals(cardCode)) {
            System.out.println("登陆成功！" + cardId);
            return R.ok().message("登陆成功！").data("账号为：",cardId);
        } else {
            return R.error().message("密码错误，请重新输入！");
        }
    }
    //创建账号
    public Account createAccount(Integer customerId, String customerName, String cardCode,Integer money) {
        if (customerId > 0) {
            Account account = new Account();
            Random random = new Random();
            Integer num = random.nextInt(1000);
            //将账号密码保存在银行之中
            HashMap<Integer,String> cardsCode = new HashMap<>();
            cardsCode.put(num,cardCode);
            bank.setCardsCode(cardsCode);
            //将账号余额保存在账户中
            account.setCardId(num);
            account.setBalance(money);
            System.out.println("创建成功");
            return account;
        } else {
            return null;
        }
    }
    //用户取款操作
    public R withdrew(Account account,int withdrewNum){
        if (withdrewNum < 0){
            System.out.println("取失败,请重新输入金额");
            return R.error();
        }else{
            accountService.accountWithdrew(account,withdrewNum);
            return R.ok();
        }
    }
    //用户存款操作
    public R depoit(Account account,int depoitNum){
        if (depoitNum < 0){
            System.out.println("存款失败，请重新输入金额");
            return R.error();
        }else {
            accountService.accountDepoit( account,depoitNum);
            return R.ok();
        }
    }
    //用户转账操作
    public R transfer(Account account,int transferNum,Account tansferAccount){
        if (transferNum < 0){
            System.out.println("转账失败，请重新输入金额");
            return R.error();
        }else {
            accountService.accoutTransfer(account, transferNum, tansferAccount);
            return R.ok();
        }
    }
    //用户查询余额操作
    public void query(Account account){
        accountService.accountQuery(account);
    }
}
