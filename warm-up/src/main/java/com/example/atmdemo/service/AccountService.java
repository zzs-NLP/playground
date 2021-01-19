package com.example.atmdemo.service;

import com.example.atmdemo.entity.Account;
import com.example.atmdemo.utils.ATMTransactions;
import com.example.atmdemo.utils.R;
import com.example.atmdemo.utils.TransferTransaction;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;


public class AccountService {
        ATMService atmService = new ATMService();
        public R accountWithdrew(Account account,int withdrewNum){
                ATMTransactions transactions = atmService.indentifies("取款");
                int b = transactions.accountTransactions(account,withdrewNum);
                if (b > 0){
                        System.out.println("操作成功");
                        System.out.println(b);
                return R.ok().message("取款操作成功！");
                }else {
                        return R.error().message("取款操作失败");
                }
        }
        public R accountDepoit(Account account,int depoitNum){
                ATMTransactions transactions = atmService.indentifies("存款");
                int b = transactions.accountTransactions(account,depoitNum);
                if (b>0){
                        System.out.println("存款操作成功，金额为："+ b );
                        return R.ok().message("存款操作成功");
                }else {
                        return R.error().message("取款操作失败");
                }
        }
        public R accoutTransfer(Account account,int num,Account transferAccount){
                TransferTransaction transaction = atmService.ATMtransfer();
                int i = transaction.transfercation(account, num, transferAccount);
                if (i > 0){
                        return R.ok().message("转账操作成功");
                }else {
                        return R.error().message("转账操作失败");
                }
        }
        public int accountQuery(Account account){
                int i = atmService.transQuery(account);
                System.out.println("余额为："+ i);
                return i;
        }

}
