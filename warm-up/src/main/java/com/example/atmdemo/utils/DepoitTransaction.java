package com.example.atmdemo.utils;

import com.example.atmdemo.entity.Account;

import java.util.HashMap;

//存款操作
public class DepoitTransaction implements ATMTransactions {
    @Override
    public int accountTransactions( Account account,int num) {
        //根据卡号查询卡内余额
        int balance  = account.getBalance();
        //存款操作
        balance = balance + num;
        return balance;
    }
}
