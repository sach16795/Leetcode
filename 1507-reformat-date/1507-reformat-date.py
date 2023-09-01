class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
        day_tmp = date.split()[0][-len(date.split()[0]):-2]
        day = day_tmp if len(day_tmp)==2 else "0" + day_tmp
        return date.split()[2]+ "-" + month[date.split()[1]] + "-" + day
        