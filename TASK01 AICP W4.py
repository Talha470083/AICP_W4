class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.num_bids = 0

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

# Displaying information for each item
for item in auction_items:
    print(f"Item {item.item_number}: {item.description} - Reserve Price: ${item.reserve_price} - Number of Bids: {item.num_bids}")

