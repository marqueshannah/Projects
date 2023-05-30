

public class InventoryItem {
	private int sku;
	private String description;
	private int quantity;
	private double unitCost;

	// constructor
	public InventoryItem(int sku, String description, int quantity, double unitCost) {
		this.sku = sku;
		this.description = description;

		// check if quantity is less than 0 or a negative number
		if (quantity < 0) {
			System.out.println("Attempt to create Inventory item " + sku + " with a negative quantity");
			System.out.println("The quantity field for item " + sku + " has been set to zero");
			this.quantity = 0;

		} else {
			this.quantity = quantity;
		}

		this.unitCost = unitCost;
	}

	public void receiveItems(int quantity) {
		if (quantity <= 0) {
			System.out.println("Receive item for item " + this.sku + " is " + quantity);

		} else {
			this.quantity = this.quantity + quantity;
		}
	}

	public void shipItems(int quantity) {
		if (this.quantity - quantity < 0) {

			System.out.println("The quantity you attempted to ship for item " + this.sku + " was " + quantity);
			System.out.println("The current quantity of item " + this.sku + " is " + this.quantity);

		} else {
			this.quantity = this.quantity - quantity;
		}
	}

	public void setQuantity(int quantity) {

		if (quantity < 0) {
			System.out.println("The quantity you attempted to define for item " + this.sku + " was " + quantity);
			System.out.println("This value must be greater than or equal to zero (0)");
			this.quantity = 0;

		} else {
			this.quantity = quantity;
		}
	}

	public int getQuantity() {
		return quantity;
	}

	public int getSku() {
		return sku;
	}

	public String getDescription() {
		return description;
	}
	
	public double getUnitCost() {
		return  + unitCost;
	}

	public String toString() {
		double val = this.quantity * this.unitCost;
		return "$" + val;
	}

}