package com.example.atmdemo.entity;

import lombok.Data;

import java.util.HashMap;

@Data
public class Account {
    private int cardId;
    private String cardType;
    private String ownedBy;
    private int balance;
    public Account(){
    }
}
