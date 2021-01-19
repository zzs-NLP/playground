package com.example.atmdemo.service;

import com.example.atmdemo.entity.Account;
import com.example.atmdemo.utils.ATMTransactions;
import com.example.atmdemo.utils.DepoitTransaction;
import com.example.atmdemo.utils.TransferTransaction;
import com.example.atmdemo.utils.WithdrewTransaction;


public class ATMService {
     ATMTransactions transactions = new ATMTransactions() {
         @Override
         public int accountTransactions(Account account, int num) {
             return 0;
         }
     };
    //工厂模式存款取款操作
    public ATMTransactions indentifies(String actionsType){

        if (actionsType.equals("取款")){
            transactions = new WithdrewTransaction();
        }
        if (actionsType.equals("存款")){
            transactions = new DepoitTransaction();
        }
        return transactions;
    }
    //ATM转账操作
    public TransferTransaction ATMtransfer(){
        TransferTransaction transaction = new TransferTransaction();
        return transaction;
    }
    //ATM查询操作
    public int transQuery(Account account) {
        int balance = account.getBalance();
        return balance;
    }


}
