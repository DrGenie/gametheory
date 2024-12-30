
import matplotlib.pyplot as plt

# Collect data
offers = []
rejections = []

print("Ultimatum Game Simulation")
for i in range(5):  # Adjust for number of rounds
    offer = float(input(f"Round {i+1} - Proposer's Offer (0-10): "))
    response = input("Responder (Accept/Reject): ").strip().lower()
    offers.append(offer)
    rejections.append(1 if response == 'reject' else 0)

# Analyze data
accepted = [offers[i] for i in range(len(offers)) if rejections[i] == 0]
rejected = [offers[i] for i in range(len(offers)) if rejections[i] == 1]

# Plot data
plt.figure(figsize=(8, 5))
plt.hist(offers, bins=5, alpha=0.5, label='All Offers')
plt.hist(accepted, bins=5, alpha=0.5, label='Accepted Offers')
plt.hist(rejected, bins=5, alpha=0.5, label='Rejected Offers')
plt.title("Ultimatum Game: Offer Analysis")
plt.xlabel("Offer Amount")
plt.ylabel("Frequency")
plt.legend()
plt.show()
