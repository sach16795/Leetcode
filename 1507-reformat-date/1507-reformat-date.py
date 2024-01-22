class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {"Jan" :"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        idx = date.split(" ")
        date = idx[0][:-2]
        month = month_map[idx[1]]
        return idx[2] + "-" + str(month) + "-" + (str(0) +str(date) if len(date) ==1 else   str(date))
        