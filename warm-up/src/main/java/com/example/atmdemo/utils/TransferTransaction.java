package com.example.atmdemo.utils;

import com.example.atmdemo.entity.Account;

import java.util.HashMap;

//转账操作
public class TransferTransaction {
    public int transfercation(Account account,int num ,Account transferAccount){
        //获取当前卡号余额
        int balance01 = account.getBalance();
        //获取转账卡内的余额
        int balance02 = transferAccount.getBalance();
        //执行转账操作
        balance01 = balance01 - num;
        if (balance01 > 0){
            balance02 = balance02 + num;
            account.setBalance(balance01);
            transferAccount.setBalance(balance02);
            System.out.println("转账金额为：" + balance02);
        }
        return balance01;
    }
}
