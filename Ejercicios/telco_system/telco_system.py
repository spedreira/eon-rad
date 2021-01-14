import datetime

COST_INTERNATIONAL_CALL_MIN = 2
COST_NATIONAL_CALL_MIN = 1.5
COST_LOCAL_CALL_MIN = 0.50
COST_LOCAL_CALL_MIN_PEAK = 1
INVALID_HOUR = 25

class TelcoSystem:
    def __init__(self, peak_hour = INVALID_HOUR):
        
        self.peak_hour = peak_hour
        self.invoices = {}
        self.invoices['all_billed'] = 0
        self.invoices['all_calls'] = 0


    @staticmethod
    def with_peak_hour_starting_at(an_hour):
        return TelcoSystem(an_hour)


    def register_international_call_between(self, start_date, end_date, client_name):
        int_cost = ((end_date - start_date).total_seconds())/60 * COST_INTERNATIONAL_CALL_MIN
        if client_name not in self.invoices:
            self.invoices[client_name] = []
            self.invoices[client_name].append((client_name, start_date.strftime('%m/%d/%Y'), 'International',str(((end_date - start_date).total_seconds())/60)+' minutes', str(int_cost)+' pesos'))
            self.invoices[client_name + ' bills'] = int_cost
            self.invoices[client_name + ' calls'] = 1
        else:
            self.invoices[client_name].append((client_name, start_date.strftime('%m/%d/%Y'), 'International',str(((end_date - start_date).total_seconds())/60)+' minutes', str(int_cost)+' pesos'))
            self.invoices[client_name + ' bills'] += int_cost
            self.invoices[client_name + ' calls'] += 1
        #####################    
        self.invoices['all_billed'] += int_cost
        self.invoices['all_calls'] += 1


    def register_national_call_between(self, start_date, end_date, client_name):
        nat_cost = ((end_date - start_date).total_seconds())/60 * COST_NATIONAL_CALL_MIN
        if client_name not in self.invoices:
            self.invoices[client_name] = []
            self.invoices[client_name].append((client_name, start_date.strftime('%m/%d/%Y'), 'National',str(((end_date - start_date).total_seconds())/60)+' minutes', str(nat_cost)+' pesos'))
            self.invoices[client_name + ' bills'] = nat_cost
            self.invoices[client_name + ' calls'] = 1
        else:
            self.invoices[client_name].append((client_name, start_date.strftime('%m/%d/%Y'), 'National',str(((end_date - start_date).total_seconds())/60)+' minutes', str(nat_cost)+' pesos'))
            self.invoices[client_name + ' bills'] += nat_cost
            self.invoices[client_name + ' calls'] += 1
        #####################    
        self.invoices['all_billed'] += nat_cost
        self.invoices['all_calls'] += 1


    def register_local_call_between(self, start_date, end_date, client_name):
        peak_minutes = 0
        minutes = 0
        date = start_date
        while (date < end_date):
            if (date.hour == self.peak_hour):
                peak_minutes += 1
                date = date + datetime.timedelta(minutes=1)
            else:
                date = date + datetime.timedelta(minutes=1)
                minutes += 1
        local_cost = minutes*COST_LOCAL_CALL_MIN + peak_minutes*COST_LOCAL_CALL_MIN_PEAK
        if client_name not in self.invoices:
            self.invoices[client_name] = []
            self.invoices[client_name].append((client_name, start_date.strftime('%m/%d/%Y'), 'Local',str(((end_date - start_date).total_seconds())/60)+' minutes', str(local_cost)+' pesos'))
            self.invoices[client_name + ' bills'] = local_cost
            self.invoices[client_name + ' calls'] = 1
        else:
            self.invoices[client_name].append((client_name, start_date.strftime('%m/%d/%Y'), 'Local',str(((end_date - start_date).total_seconds())/60)+' minutes', str(local_cost)+' pesos'))
            self.invoices[client_name + ' bills'] += local_cost
            self.invoices[client_name + ' calls'] += 1
        #####################    
        self.invoices['all_billed'] += local_cost
        self.invoices['all_calls'] += 1


    def historical_total_billed(self):
        print(self.invoices['all_billed'])

    
    def historical_number_of_calls(self):
        print(self.invoices['all_calls'])
        

    def total_billed_for(self, client_name):
        print(self.invoices[client_name + ' bills'])


    def number_of_calls_for(self, client_name):
        print(self.invoices[client_name + ' calls'])

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