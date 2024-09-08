create table client_master
(
  client_no varchar(6) primary key,
  name varchar(20) not null,
  city varchar(15),
  state varchar(15),
  pincode decimal(6),
  bal_due decimal(10,2),
  check(client_no like 'C%')
);
select * from  client_master;
create table product_master
(
 product_no varchar(6) primary key,
 description varchar(15) not null,
 profit_percent decimal(2,2) not null,
 unit_measure varchar(10) not null,
 qty_on_hand decimal(8) not null,
 reorder_lvl decimal(8) not null,
 sell_price decimal(8,2) not null, 
 cost_price decimal(8,2) not null, 
 check(product_no like 'P%' and sell_price<>0 and cost_price<>0)
 );
 select * from product_master;
 create table salesman_master
 (
  salesman_no varchar(6) primary key,
  salesman_name varchar(20) not null,
  address1 varchar(30) not null,
  address2 varchar(30),
  city varchar(20),
  pincode varchar(6),
  state varchar(20),
  sal_amt decimal(8,2) not null,
  tgt_to_get decimal(6,2) not null,
  ytd_sales decimal(6,2) not null,
  remarks varchar(60),
  check(salesman_no like 'P%' and sal_amt<>0 and tgt_to_get<>0)
  );
  create table sales_order
  (
   s_order_no varchar(6) primary key,
   s_order_date Date,
   client_no varchar(6) ,
   salesman_no varchar(6),
   dely_type char(1),
   billed_yn char(1),
   dely_date date,
   order_status varchar(10),
   check(s_order_no like 'O%'),
   check(order_status in('IP' , 'F' , 'BO' , 'C')),
   check(dely_type>s_order_date),
   foreign key(client_no) references client_master(client_no),
   foreign key(salesman_no) references salesman_master(salesman_no),
   check(dely_type in('P' , 'F'))
   );
   create table sales_order_details
   (
    s_order_no varchar(6) references sales_order(s_order_no),
    product_no varchar(6) references product_master(product_no),
    qty_ordered decimal(8),
    qty_disp decimal(8),
    product_rate decimal(10,2),
    primary key(s_order_no,product_no)
    );
    create table Challan_header
    (
     challan_no varchar(6) primary key,
     s_order_no varchar(6),
     challan_date date not null,
     foreign key(s_order_no) references sales_order(s_order_no),
     billed_yn char(1) default 'N',
     check(challan_no like 'CH%')
     );
     create table challan_details
     (
      challan_no varchar(6),
      foreign key(challan_no) references Challan_header(challan_no),
      product_no varchar(6),
      foreign key(product_no) references product_master(product_no),
      qty_disp decimal(4,2) not null,
      primary key(challan_no,product_no)
      );
insert into salesman_master values(
'P00001','Kiran','A/14','Worli','Bombay',400002,'MAH',3000,100,50,'Good'
);
insert into salesman_master values(
'P00002','Manish','65','Nariman','Bombay',400001,'MAH',3000,200,100,'Good'
);
insert into salesman_master values(
'P00003','Ravi','P-7','Bandra','Bombay',400032,'MAH',3000,200,100,'Good'
# );
insert into salesman_master values(
'P00004','Ashish','A/5','Juhu','Bombay',400044,'MAH',3500,200,150,'Good'
);
select * from salesman_master;

insert into client_master values ('C00001', 'Ivan Bayross', 'Bombay', 'Maharashtra', 400054, 15000);
insert into client_master values ('C00002', 'Vandana Saitwal', 'Madras', 'Tamil Nadu', 780001, 0);
insert into client_master values ('C00003', 'Parmada Jaguste', 'Bombay', 'Maharashtra', 400057, 5000);
insert into client_master values ('C00004', 'Basu Navindgi', 'Bombay', 'Maharashtra', 400056, 0);
insert into client_master values ('C00005', 'Ravi Sreedharan', 'Delhi', ' ', 100001, 2000);
insert into client_master values ('C00006', 'Rukmini', 'Bombay', 'Maharashtra', 400050, 0);
      
      select * from client_master;
insert into sales_order_details values ('019001', 'P00001', 4,
4, 525);
insert into sales_order_details values ('019002', 'PO7965', 2,
1, 8400);
insert into sales_order_details values ('019003', ' P0785', 2,
1, 5250);
insert into sales_order_details values ('019004', 'P00001', 10,
0, 525);
insert into sales_order_details values ('019005', 'P07868', 3,
3, 3150);
insert into sales_order_details values ('019006', ' P0785', 3,
1, 5250);
insert into sales_order_details values ('019007', 'PO0001', 10,
# insert into sales_order_details values ('019007', 'PO0001', 10,
10, 525);
insert into sales_order_details values ('019008', 'PO331', 4,
4, 1050);
insert into sales_order_details values ('019009', 'PO3453', 2,
2, 1050);
insert into sales_order_details values ('019010', 'P06734', 1,
1, 12000);
insert into sales_order_details values ('019011', 'P07965', 1,
0, 8400) ;
insert into sales_order_details values ('019012', 'PO7975', 1,
0, 1050);
insert into sales_order_details values ('019013', 'P00001', 10,
5, 525) ;
insert into sales_order_details values ('019014', 'P07975', 5,
3, 1050) ;
       select * from sales_order_details;
insert into sales_order values ('O19001','1996-01-12','C00001', 'S00001','F', 'N', '1996-01-20', 'IP');
insert into sales_order values('O19002','1996-01-25','C00002', 'S00002', 'P', 'N','1996-01-27', 'C');
insert into sales_order values
('O46865', '1996-02-18','C00003', 'S00003','F', 'y', '1996-02-20', 'F');
insert into sales_order values
('O19003','1996-04-03','C00001','S00001', 'F', 'Y','1996-04-07', 'F');
insert into sales_order values
('O46866', '1996-05-20', 'C00004', 'S00002', 'P', 'N','1996-05-22', 'C');
insert into sales_order values
('O10008','1996-05-24', 'C00005', 'S00004', 'F', 'N','1996-05-26', 'IP')
create table product_master1
(
 product_no varchar(6) primary key,
 description varchar(15) not null,
 profit_percent decimal(4,2) not null,
 unit_measure varchar(10) not null,
 qty_on_hand decimal(8) not null,
 reorder_lvl decimal(8) not null,
 sell_price decimal(8,2) not null, 
 cost_price decimal(8,2) not null, 
 check(product_no like 'P%' and sell_price<>0 and cost_price<>0)
 );
 select * from product_master1;
 desc product_master1;
insert into product_master1 values( 'P00001' , '1.44 Floppies' , 5 , 'Piece' , 100 , 20 , 525 , 500);
 
 insert into product_master1 values( 'P03453' , 'Monitors' , 6 , 'Piece' , 10 , 3 , 12000 , 11280);
 insert into product_master1 values( 'P06734' , 'Mouse' , 5 , 'Piece' , 20 , 5 , 1050 , 1000);
 insert into product_master1 values( 'P07865' , '1.22 Floppies' , 5 , 'Piece' , 100 , 20 , 525 , 500);
 insert into product_master1 values( 'P07868' , 'Keyboards' , 2 , 'Piece' , 10 , 3 , 3150 , 3050);
 insert into product_master1 values( 'P07885' , 'CD Drive' , 2.5 , 'Piece' , 10 , 3 , 5250 , 5100);
 insert into product_master1 values( 'P07965' , '540 HDD' , 4 , 'Piece' , 10 , 3 , 8400 , 8000);
 insert into product_master1 values( 'P07975' , '1.44 Drive' , 5 , 'Piece' , 100 , 20 , 1050 , 1000);
 insert into product_master1 values( 'P08865' , '1.22 Drive' , 5 , 'Piece' , 2 , 3 , 1050 , 1000);
 select * from product_master1;