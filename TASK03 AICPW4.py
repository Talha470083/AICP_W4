class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.num_bids = 0
        self.highest_bid = 0
        self.sold = False

    def view_details(self):
        print(f"Item {self.item_number}: {self.description} - Reserve Price: ${self.reserve_price} - Highest Bid: ${self.highest_bid} - Number of Bids: {self.num_bids}")

    def record_bid(self, buyer_number, bid_amount):
        if bid_amount > self.highest_bid and bid_amount >= self.reserve_price:
            self.highest_bid = bid_amount
            self.num_bids += 1
            print(f"Bid recorded successfully for Item {self.item_number} by Buyer {buyer_number}. New highest bid: ${self.highest_bid}")
        else:
            print(f"Bid rejected for Item {self.item_number}. Please enter a higher bid.")

    def mark_as_sold(self):
        self.sold = True

def main():
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
    print("------------------------------")


# Identify items that have reached their reserve price and mark them as sold
total_fee = 0
items_sold = 0
items_not_met_reserve = 0
items_no_bids = 0

for item in auction_items:
    if item.highest_bid >= item.reserve_price:
        item.mark_as_sold()
        items_sold += 1
        auction_fee = 0.1 * item.highest_bid
        total_fee += auction_fee
        print(f"Item {item.item_number} - SOLD! Final Bid: ${item.highest_bid} - Auction Fee: ${auction_fee}")
    else:
        if item.num_bids == 0:
            items_no_bids += 1
            print(f"Item {item.item_number} - No Bids Received.")
        else:
            items_not_met_reserve += 1
            print(f"Item {item.item_number} - Highest Bid: ${item.highest_bid} - Did not meet the reserve price.")

# Displaying summary information
print("\nSummary:")
print(f"Total Auction Fee for Sold Items: ${total_fee}")
print(f"Number of Items Sold: {items_sold}")
print(f"Number of Items Not Meeting Reserve Price: {items_not_met_reserve}")
print(f"Number of Items with No Bids: {items_no_bids}")
if __name__ == "__main__":
    main()

