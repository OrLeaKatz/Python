m = [[False]*10]*8

class Cinema_room:
    def __init__(self,Movie):
        self.matrixChair = [[False for j in range(8)]for i in range (10)]
        self.movie = Movie


    def order_seats(self,amount):
        for row in range(len(self.matrixChair)):
            for col in range(len(self.matrixChair[row])):
                if not self.matrixChair[row][col]:
                    self.matrixChair[row][col] = True
                    amount -=1
                    if amount == 0:
                        return True
        return False

    def get_info(self):
        seat_status="\n"
        for row in range(0,len(self.matrixChair)):
            for col in range(0,len(self.matrixChair[row])):
                if self.matrixChair[row][col]:
                    seat_status+=" V |"
                else:
                    seat_status+=" X |"
            seat_status+="\n----------------------------------\n"
        return self.movie.get_info() + seat_status
    