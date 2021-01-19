package com.example.atmdemo.entity;

import lombok.Data;

import java.util.HashMap;
import java.util.List;

@Data
public class Bank {
    private HashMap<Integer,String> cardsCode;
    private static Bank bank;
    private Bank(){
    }

    public static Bank getInstance(){
        if (bank == null){
            bank = new Bank();
        }
        return bank;
    }
}
