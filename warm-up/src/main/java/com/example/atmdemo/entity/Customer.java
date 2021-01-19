package com.example.atmdemo.entity;
import lombok.Data;

import java.util.List;

@Data
public class Customer {
    private int customerID;
    private String customerName;
    private Card card;
    public Customer(){};
    public Customer(int CID, String name){
        this.customerID = CID;
        this.customerName = name;
    }
}
