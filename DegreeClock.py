class clock:
    def __init__(self):
        self.hour = 1
        self.min = 1
    def calculateDegree(self):
        minuteRevisedToHour = self.min / 5
        distanceBWneedle = self.hour - minuteRevisedToHour
        finalDegree = distanceBWneedle * 5 * 6
        if finalDegree > 180:
             finalDegree -= 360
        return finalDegree

    def printResult(self, result):
        print "The Degree bw in time ", self.hour, ":", self.min, " is : ", abs(result)

clockObject = clock()
result = clockObject.calculateDegree()
clockObject.printResult(result)
