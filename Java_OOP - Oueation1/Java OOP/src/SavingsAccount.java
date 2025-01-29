public class SavingsAccount extends Account {

    SavingsAccount(double balance, double interestRate) throws Exception{
      if(balance > 0){
        setBalance(balance);
      }
      else{
        throw new Exception("Balance cannot be negative");
      }
      setInterestRate(interestRate);
  
    }
  
    @Override
    public double calculateInterest() {
      return getBalance() +  getBalance() * (1 + getInterestRate())-getBalance();
    }
  
  }