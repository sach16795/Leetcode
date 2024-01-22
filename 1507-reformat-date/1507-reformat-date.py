class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {"Jan" :"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        idx = date.split(" ")
        return idx[2] + "-" + month_map[idx[1]] + "-" + (str(0) +str(idx[0][:-2]) if len(idx[0][:-2]) ==1 else   str(idx[0][:-2]))
        