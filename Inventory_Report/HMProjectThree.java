import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Scanner;
import java.util.Set;

//Student: Hannah Marques 
public class HMProjectThree { //default paths for 
	private static String FILEPAT_ITEM;
	private static String FILEPAT_ACTIVITY ;
	private static String REPORT;

	public static void createReportFile(ArrayList<InventoryItem> items) {
		try {
                    //prompt the user for the report path
                        Scanner filereportname = new Scanner (System.in);
                        System.out.println("insert path for report: ");
                        String FILEPAT_REPORT = filereportname.nextLine();
			NumberFormat newFormat = NumberFormat.getInstance();
			Date date = new Date();
			DateFormat sdf = new SimpleDateFormat("EEEE, MMMM dd, yyyy HH:mm:ss");
			String stringDate = sdf.format(date);
                       //write in report.txt
                    try (FileWriter report = new FileWriter(FILEPAT_REPORT)) {
                        report.write("\t\t\t\t\t\t\t\tJohn Smith for the Ragnarok Company, Inc.\n");
                        report.write("\t\t\t\t\t\t\tPrepared On : " + stringDate + "\n\n");
                        report.write("\t\t\t\t\t\t\t I N V E N T O R Y   R E P O R T\n\n");
                        report.write("Item Inventory\n");
                        report.write(String.format("%1s %30s %35s %19s %24s", "Number", "Description", "Quantity", "Unit Price",
                                "Value"));
                        report.write("\n");
                        
                        for (InventoryItem item : items) {
                            double val = Double.parseDouble(item.toString().replace("$", ""));
                            report.write(String.format("%1s %30s %35s %19s %25s", item.getSku(), item.getDescription(),
                                    item.getQuantity(), item.getUnitCost(), newFormat.format(val)));
                            report.write("\n");
                        }
                    }
                    REPORT = FILEPAT_REPORT;

		} catch (IOException | NumberFormatException e) {
			System.out.println("ERROR: Cannot create report  " + e.getMessage());
		}
	}

	public static LinkedHashMap<Integer, InventoryItem> readItemFile(String FileName) {
		LinkedHashMap<Integer, InventoryItem> items = new LinkedHashMap<>();
                 //prompt the user to enter items.txt path
		try {
                    Scanner itemsFile = new Scanner(System.in);
                System.out.println( "Enter items file path: ");
                FILEPAT_ITEM = itemsFile.nextLine()   ;
                    

			File file = new File(FILEPAT_ITEM);
			FileReader read = new FileReader(file);
			BufferedReader br = new BufferedReader(read);
			String line;
			int ctr = 0;

			while ((line = br.readLine()) != null) {

				String[] arr = line.split(",");
				InventoryItem item = new InventoryItem(Integer.parseInt(arr[0]), arr[1], Integer.parseInt(arr[2]),
						Double.parseDouble(arr[3]));
				items.put(Integer.parseInt(arr[0]), item);
				ctr++;
			}
			read.close();

			System.out.println(ctr + " inventory items have been created");

		} catch (IOException | NumberFormatException e) {
			System.out.println("ERROR : invalid item filename");
		}

		return items;
	}

	public static ArrayList<String> readActivityFile(String fileName) {
		ArrayList<String> activity = new ArrayList<String>();
               //prompt the user to enter activity.txt path
		try {
                     Scanner activityFile = new Scanner(System.in);
                     System.out.println( "Enter activity file path: ");
                     FILEPAT_ACTIVITY = activityFile.nextLine() ;
                     

			File file = new File(FILEPAT_ACTIVITY);
			FileReader read = new FileReader(file);
			BufferedReader br = new BufferedReader(read);
			String line;

			while ((line = br.readLine()) != null) {
				activity.add(line);
			}

		} catch (IOException e) {
			System.out.println("ERROR : invalid activity filename");
		}

		return activity;
	}

	public static boolean isSKUInActivity(int sku, ArrayList<String> activities) {
		for (String activity : activities) {
			if (activity.contains(Integer.toString(sku))) {
				return true;
			}
		}

		return false;
	}
         //get total
	public static double getTotalValue(ArrayList<InventoryItem> list) {
		double total = 0;
		for (InventoryItem item : list) {
			String strTotal = item.toString().replace("$", "");
			double totalConv = Double.parseDouble(strTotal);
			total += totalConv;
		}
		return Math.round(total * 100.0) / 100.0;
	}

	public static void main(String[] args) throws IOException {
		NumberFormat newFormat = NumberFormat.getInstance();

		int ctr = 1, skipCnt = 0, quantityCnt = 0;

		LinkedHashMap<Integer, InventoryItem> items = readItemFile(FILEPAT_ITEM);

		ArrayList<InventoryItem> newItems = new ArrayList<>();
		HashMap<String, InventoryItem> newItemsMap = new HashMap<>();
		//newItemsMap.co

		ArrayList<String> activities = readActivityFile(FILEPAT_ACTIVITY);

		Set<Integer> keys = items.keySet();

		for (int sku : keys) {
			InventoryItem item = items.get(sku);

			if (isSKUInActivity(sku, activities)) {
				for (String activity : activities) {
					String[] arr = activity.split(",");

					if (arr[1].equals(Integer.toString(sku))) {
						switch (arr[0]) {

						case "D":
							item.setQuantity(Integer.parseInt(arr[2]));
							//newItems.add(item);
							newItemsMap.put(arr[1], item);
							break;

						case "R":
							item.receiveItems(Integer.parseInt(arr[2]));
							//newItems.add(item);
							newItemsMap.put(arr[1], item);
							quantityCnt++;
							break;

						case "S":
							item.shipItems(Integer.parseInt(arr[2]));
							//newItems.add(item);
							newItemsMap.put(arr[1], item);
							quantityCnt++;
							break;

						default:
							System.out.println("Bad Transaction Code: " + arr[0] + " in record " + ctr);
							skipCnt++;
						}
					}
				}

			} else {
				//newItems.add(item);
				newItemsMap.put(item.getSku() + "", item);
			}

			ctr++;
		}
		Collection values = newItemsMap.values();
		newItems = new ArrayList(values);
		createReportFile(newItems);

		System.out.println(items.size() - skipCnt + " records processed; " + skipCnt + " records skipped");
		System.out.println(quantityCnt + " inventory item quantity transactions");
		System.out.println("Total Inventory Value is $" + newFormat.format(getTotalValue(newItems)));
                double runningtotal = (getTotalValue(newItems));
        
         
        usingBufferedWritter(runningtotal);
        
        }
        //print total formated 
        public static void usingBufferedWritter(double runningtotal) throws IOException 
{        DecimalFormat df = new DecimalFormat("#,###.00");
            
    String textToAppend =String.format("%1$110s", "Total: " ) ;
 
            try ( //Set true for append mode
                    
                    BufferedWriter writer = new BufferedWriter(
                            new FileWriter(REPORT, true))) {
                writer.write(textToAppend + df.format(runningtotal));
            }
}
	
	
	private static InventoryItem getUpdatedItem(InventoryItem item) {
		
		
		return null;
	}

}
