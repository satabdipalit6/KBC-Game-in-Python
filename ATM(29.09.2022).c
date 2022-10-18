#include<stdio.h>
#include<conio.h>
void main()
{
	 system("color 3F");
	 time_t t = time(NULL);
     printf("\n");
     printf("\t \t \t \t \t%s", ctime(&t));
     int pin=8520,enteredpin,c=1,ch,ch1,amt,balance=5000,r1,r2,pin1;
     start:
     //---------------------------Authentication--------------------------------
     
     printf("\n\t\t==============================================================\n");
     printf("\n\t\t==                      LOGIN PAGE                          ==\n");
     printf("\n\t\t==                                                          ==\n");
     printf("\n\t\t==============================================================\n");
     printf("\n \n ");
     printf("\n Enter you pin=");
     scanf("%d",&enteredpin);
     if(pin==enteredpin)
     {
     	system("CLS");
     	printf("\n\t\t==============================================================\n");
        printf("\n\t\t==              Welcome to ATM SERVICE                      ==\n");
        printf("\n\t\t==                                                          ==\n");
        printf("\n\t\t==============================================================\n");	
		
		printf("\n Please Select your choice \n");	
		printf("\n 1. Deposit ");
		printf("\n 2. Withdraw" );
		printf("\n 3. Balance Enquiry");
		printf("\n 4. Pin Change");
		printf("\n 5. Logout ");
		printf("\n");
		scanf("%d",&ch);						
		switch(ch)
		{
	           case 1: 
			        printf("\n Enter the deposit amount=");
			        scanf("%d",&amt);
			        r1=amt/100; r2=amt/500;
			        printf("\n You have %d 100 rupees note",r1);
			        printf("\n OR ");
			        printf("\n You have %d 500 rupees note",r2 );
			        
	                   if(amt<=20000)
	                   {
	                   	  balance=balance + amt;
	                   	  printf("\n After deposit your balance is=%d",balance);
					   }
					   else
					   {
					   	  printf("\n  Today's max limit of deposit is 20000. ");
					   }
	                break;
	                
	            case 2:    
	                printf("\n Enter the withdraw amount=");
			        scanf("%d",&amt);
			        if(amt%100==0 || amt%500==0)
			        {
			        	if(balance<amt)
	                   {
	                   	   
	                   	  printf("\n Your Balance is insufficient ");
					   }
					   else
					   {
					   	  if(amt<=20000)
					      {
					      	balance=balance - amt;
					      	printf("\n Withdraw amount is %d, \n your available balance is %d",amt,balance);
						  }
						  else
						  {
						  	printf("\n You exceed the daily withdrawal limit ");
						  }
					   }
					}
					else
					{
						printf("\n Withdraw amount is not multiple of 100 or 500 ");
					}
	                   
	                break;  
	                
				case 3:  
				     printf("\n Available Balance is %d",balance);
				     break;
				     
				case 4:	
				     printf("\n Enter your new pin=");  
					 scanf("%d",&pin);   
					 printf("\n Confirm your new pin=");  
					 scanf("%d",&pin1); 
					 if(pin==pin1)
					   printf("\n Your pin has been changed successfully!.....");
					 else
					 {
					 	printf("\n Sorry you have entered wrong pin.."); 
					 	pin=8520;
					 }
					    
					 break;
			    case 5:
				    printf("\n\n... Thank you for visiting ATM...");
				    exit(0);
				    		 
	           default:
		            printf("\n Sorry You have entered worng choice ");	   
					goto start; 
		            
		           
		}
       printf("\n Do you want another transaction,(type 0  or 1)");	
       scanf("%d",&ch1);
       if(ch1==1)
       {
       	  goto start;
	   }
	   else
	   {
	   	printf("\n... Thank you for visiting ATM...");
	   }
       
	 }
	 else
	 {
	 	printf("\n Sorry,You have invalid pin");
	 	sleep(5);
	 	system("CLS");
	 	if(c<3)
	 	{   c++;
	 		goto start;
		}
		else{
			printf("\n Today's limit of number of attempts is exceeded'");
		}
	 	
	 }
	 
	 
}
