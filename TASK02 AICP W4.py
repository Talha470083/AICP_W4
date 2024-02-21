class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.num_bids = 0
        self.highest_bid = 0

    def view_details(self):
        print(f"Item {self.item_number}: {self.description} - Reserve Price: ${self.reserve_price} - Highest Bid: ${self.highest_bid} - Number of Bids: {self.num_bids}")

    def record_bid(self, buyer_number, bid_amount):
        if bid_amount > self.highest_bid and bid_amount >= self.reserve_price:
            self.highest_bid = bid_amount
            self.num_bids += 1
            print(f"Bid recorded successfully for Item {self.item_number} by Buyer {buyer_number}. New highest bid: ${self.highest_bid}")
        else:
            print(f"Bid rejected for Item {self.item_number}. Please enter a higher bid.")

# Creating a list to store auction items
auction_items = []

# Adding at least 10 items to the auction
auction_items.append(AuctionItem(1, "Painting", 500))
auction_items.append(AuctionItem(2, "Antique Vase", 1000))
auction_items.append(AuctionItem(3, "Vintage Watch", 800))
auction_items.append(AuctionItem(4, "Rare Book", 300))
auction_items.append(AuctionItem(5, "Sculpture", 700))
auction_items.append(AuctionItem(6, "Collectible Coins", 1200))
auction_items.append(AuctionItem(7, "Jewelry Set", 900))
auction_items.append(AuctionItem(8, "Classic Car", 5000))
auction_items.append(AuctionItem(9, "Designer Handbag", 600))
auction_items.append(AuctionItem(10, "Electronics Bundle", 1500))

# Simulating buyer bids
buyer_number = 1
for item in auction_items:
    item.view_details()
    bid_amount = int(input(f"Enter your bid for Item {item.item_number}: $"))
    item.record_bid(buyer_number, bid_amount)

