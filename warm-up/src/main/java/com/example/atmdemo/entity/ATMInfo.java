package com.example.atmdemo.entity;

import com.example.atmdemo.utils.ATMTransactions;
import com.example.atmdemo.utils.WithdrewTransaction;
import lombok.Data;

@Data
public class ATMInfo {
    private String location;
    private String mangedBy;


}
