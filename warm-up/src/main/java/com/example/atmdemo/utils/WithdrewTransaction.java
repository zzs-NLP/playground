package com.example.atmdemo.utils;

import com.example.atmdemo.entity.Account;
import com.example.atmdemo.utils.ATMTransactions;
import com.example.atmdemo.utils.R;

import java.util.HashMap;

public class WithdrewTransaction implements ATMTransactions {
    @Override
    public int accountTransactions(Account account,int num) {
        //根据卡号查询卡内余额
        int balance  = account.getBalance();
        //取款操作
        balance = balance - num;
        if (balance < 0){
            return -1;
        }else {
            account.setBalance(balance);
            return balance;
        }
    }
}
