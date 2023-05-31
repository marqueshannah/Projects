//by Hannah Marques

//create a CreditCsrd class
public class CreditCard {
 private Person owner;
 private Money balance;
 private Money creditLimit;

 //contructor for credit card 
  public CreditCard(Person newCardHolder, Money limit)
   {
    owner = newCardHolder;
    creditLimit = limit;
    balance = new Money(0);
   }
  public Money getBalance(){
   
    Money temp = new Money(balance);
    return balance;
  }
  
  public Money getCreditLimit()
  {
    Money temp = new Money(creditLimit);
    return creditLimit;
  }
  public String getPersonals()
   {
     return owner.toString();
   }
  public void charge(Money amount)
  {
    if(balance.add(amount).compareTo(creditLimit) < 0)
     {
      System.out.println("Charge: " + balance);
      balance = balance.add(amount); 
     }
    else
     {
       System.out.println("EXCEEDS CREDIT LIMIT");
     }
}
   public void payment(Money amount)
   {
   System.out.println("Payment: " + amount);
   balance = balance.subtract(amount);

   }
}
