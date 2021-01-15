import datetime

INVALID_HOUR = 25

class InternationalCall():
    call_cost_per_min = 2
    
    def bill(start_date, end_date, client_name, int_cost):
        #Client Name, Class, Length, Cost
        return (client_name, start_date.strftime('%m/%d/%Y'), 'International',str(((end_date - start_date).total_seconds())/60)+' minutes', str(int_cost)+' pesos')

class NationalCall():
    call_cost_per_min = 1.5

    def bill(start_date, end_date, client_name, nat_cost):
        #Client Name, Class, Length, Cost
        return (client_name, start_date.strftime('%m/%d/%Y'), 'National',str(((end_date - start_date).total_seconds())/60)+' minutes', str(nat_cost)+' pesos')

class LocalCall():
    call_cost_per_min = 0.5
    call_cost_per_min_peak_hour = 1

    def bill(start_date, end_date, client_name, local_cost):
        #Client Name, Class, Length, Cost
        return (client_name, start_date.strftime('%m/%d/%Y'), 'Local',str(((end_date - start_date).total_seconds())/60)+' minutes', str(local_cost)+' pesos')


class TelcoSystem:
    def __init__(self, peak_hour = INVALID_HOUR):
        
        self.peak_hour = peak_hour
        self.invoices = {}
        self.all_billed = 0
        self.all_calls = 0


    @staticmethod
    def with_peak_hour_starting_at(an_hour):
        return TelcoSystem(an_hour)


    def register_international_call_between(self, start_date, end_date, client_name):
        int_cost = ((end_date - start_date).total_seconds())/60 * InternationalCall.call_cost_per_min

        if client_name not in self.invoices:
            self.invoices[client_name] = []
            self.invoices[client_name].append(InternationalCall.bill(start_date, end_date, client_name, int_cost))
            self.invoices[client_name + ' bills'] = int_cost
        else:
            self.invoices[client_name].append(InternationalCall.bill(start_date, end_date, client_name, int_cost))
            self.invoices[client_name + ' bills'] += int_cost
        #####################    
        self.all_billed += int_cost
        self.all_calls += 1


    def register_national_call_between(self, start_date, end_date, client_name):
        nat_cost = ((end_date - start_date).total_seconds())/60 * NationalCall.call_cost_per_min

        if client_name not in self.invoices:
            self.invoices[client_name] = []
            self.invoices[client_name].append(NationalCall.bill(start_date, end_date, client_name, nat_cost))
            self.invoices[client_name + ' bills'] = nat_cost
        else:
            self.invoices[client_name].append(NationalCall.bill(start_date, end_date, client_name, nat_cost))
            self.invoices[client_name + ' bills'] += nat_cost
        #####################    
        self.all_billed += nat_cost
        self.all_calls += 1


    def register_local_call_between(self, start_date, end_date, client_name):
        peak_minutes = 0
        minutes = 0
        date = start_date
        while (date < end_date): #minutes in a peak hour
            if (date.hour == self.peak_hour):
                peak_minutes += 1
                date = date + datetime.timedelta(minutes=1)
            else:
                date = date + datetime.timedelta(minutes=1)
                minutes += 1
        local_cost = minutes*LocalCall.call_cost_per_min + peak_minutes*LocalCall.call_cost_per_min_peak_hour

        if client_name not in self.invoices:
            self.invoices[client_name] = []
            self.invoices[client_name].append(LocalCall.bill(start_date, end_date, client_name, local_cost))
            self.invoices[client_name + ' bills'] = local_cost
        else:
            self.invoices[client_name].append(LocalCall.bill(start_date, end_date, client_name, local_cost))
            self.invoices[client_name + ' bills'] += local_cost
        #####################    
        self.all_billed += local_cost
        self.all_calls += 1


    def historical_total_billed(self):
        print(self.all_billed)

    
    def historical_number_of_calls(self):
        print(self.all_calls)
        

    def total_billed_for(self, client_name):
        print(self.invoices[client_name + ' bills'])


    def number_of_calls_for(self, client_name):
        print(len(self.invoices[client_name]))

    def invoices_of (self, client_name):
        print(self.invoices[client_name])
        


telco_system = TelcoSystem.with_peak_hour_starting_at(18)
x = datetime.datetime(2020, 5, 1, 18, 0, 0)

telco_system.register_local_call_between(x, x + datetime.timedelta(minutes=2), "Wanda")
telco_system.register_local_call_between(x, x + datetime.timedelta(minutes=2), "Exe")
telco_system.register_local_call_between(x, x + datetime.timedelta(minutes=2), "Exe")
telco_system.register_national_call_between(x, x + datetime.timedelta(minutes=2), "Exe")
telco_system.register_international_call_between(x, x + datetime.timedelta(minutes=2), "Exe")

telco_system.number_of_calls_for('Exe')
telco_system.total_billed_for('Exe')
telco_system.number_of_calls_for('Wanda')
telco_system.total_billed_for('Wanda')

telco_system.historical_total_billed()
telco_system.historical_number_of_calls()

telco_system.invoices_of('Exe')
telco_system.invoices_of('Wanda')