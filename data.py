import datetime as dtm
        
class datas:
    def formatar_hoje(self):
        hoje = dtm.datetime.today()
        data = dtm.datetime(hoje.year,hoje.month,hoje.day)
        return(data.__format__('%d/%m/%Y'))
    
    def formatar_hoje_inicio(self):
        hoje = dtm.datetime.today()
        data = dtm.datetime(hoje.year,hoje.month,1)
        return(data.__format__('%d/%m/%Y'))
    
    def formatar_passado_fim(self):
        hoje = dtm.datetime.today()
        data = dtm.datetime(hoje.year, hoje.month, 1)
        datafim = data - dtm.timedelta(days=1)
        return(datafim.__format__('%d/%m/%Y'))
    
    def formatar_passado_inicio(self):
        hoje = dtm.datetime.today()
        data = dtm.datetime(hoje.year, (hoje.month)-1, 1)
        return(data.__format__('%d/%m/%Y'))