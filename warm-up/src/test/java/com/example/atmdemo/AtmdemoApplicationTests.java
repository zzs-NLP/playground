package com.example.atmdemo;

import com.example.atmdemo.entity.Account;
import com.example.atmdemo.service.CustomerService;
import com.example.atmdemo.utils.R;
import org.junit.Before;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class AtmdemoApplicationTests {
    CustomerService customerService = new CustomerService();

    @Test
    void textwithdrew() {
        Account account = customerService.createAccount(123, "张三", "1234",100);
        customerService.withdrew(account,70);
    }
    @Test
    void textdepoit() {
        Account account = customerService.createAccount(123, "张三", "1234",100);
        customerService.depoit(account,70);
    }
    @Test
    void testCreate(){
       customerService.createAccount(123, "张三", "1234",100);

    }
    @Test
    void testTransfer(){
        Account account01 = customerService.createAccount(123, "张三", "1234", 100);
        Account account02 = customerService.createAccount(132, "李四", "1232", 120);
        customerService.transfer(account01,30,account02);
    }
    @Test
    void testQuery(){
        Account account01 = customerService.createAccount(123, "张三", "1234", 100);
        customerService.query(account01);
    }

}
