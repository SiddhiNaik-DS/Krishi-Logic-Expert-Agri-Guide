**🌱Krishi-Logic: Expert Agri-Guide**

Krishi-Logic: Expert Agri-Guide is an intelligent, multi-stage decision-support web application engineered in Python using the Streamlit framework. Built specifically to empower modern farmers, agricultural students, and agribusiness operators, it acts as a digital consultant that structures the entire lifecycle of crop management.
Key Features & Workflow Lifecycle:
The application uses state tracking to safely guide a user linearly through 6 progressive stages of a seasonal cultivation project:

Interactive Variety Hub (Setup): Features a built-in database of 100 crop variants across 10 categories (Vegetables, Cash Crops, Medicinal Plants, etc.). It filters seasonal options based on your financial budget.

Dynamic Agronomic Advisories: As users advance through Land Preparation, Sowing, and Nutrition/Irrigation, the app maps local conditions like soil quality and temperature against ideal crop baseline metrics. It serves real-time alerts on split fertilizer dosing, seed spacing geometries, and heat stress.

Yield Risk Prevention (Harvesting): Tracks critical harvest metrics like ideal grain or crop moisture levels to flag post-harvest storage mold hazards before they happen.

Market & Revenue Optimizer: Calculates exact economic parameters. By overlaying expected Mandi wholesale costs against your physical overhead expenses and target profit margins per unit, the app generates automated suggested pricing models and calculates total seasonal revenue projections.
🚜 Krishi-Logic: Project Setup<img width="1915" height="1016" alt="image" src="https://github.com/user-attachments/assets/45712101-fbc9-466f-bdc3-c33b29ae4b17" />
🚜 Stage 1: Detailed Land Preparation<img width="1919" height="1018" alt="image" src="https://github.com/user-attachments/assets/a3c5a56a-9835-469b-a240-d2e413788ba1" />
🌱 Stage 2: Sowing & Seed Treatment<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/edd437b7-b559-4c4b-b10e-4aea6fd32d19" />
💧 Stage 3: Nutrition & Irrigation<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/dd3f7cb6-c1dc-4a7b-91b1-cf538202c969" />
🌾 Stage 4: Harvest & Post-Harvest<img width="1919" height="1018" alt="image" src="https://github.com/user-attachments/assets/cddec36d-7c05-4d3b-b3b3-bf85d5da6fb0" />
💰 Stage 5: Market & Sales Optimizer<img width="1919" height="1016" alt="image" src="https://github.com/user-attachments/assets/135b7540-0e3c-4254-b226-8b2daaac00d1" />
Here is a comprehensive, step-by-step agronomic and operational guide to navigating a crop management lifecycle using **Krishi-Logic**:

---

### Step 1: Initialization & Project Setup

When you launch the application, you enter the **Project Setup** configuration hub.

1. **Choose a Crop Category:** Select one of the 10 master agricultural classifications from the drop-down menu (e.g., Vegetables, Fruits, Grains/Cereals, Spices, Cash Crops, etc.).
2. **Select Variety Focus:** Choose a specific crop variant from the populated list. The interface dynamically retrieves the crop's ideal baseline environmental data from the master database:
* **Optimal Growth Temperature Range** (e.g., 18–27°C for Tomatoes)
* **Water Requirement Profile** (Low, Moderate, High, or Very High)


3. **Allocate Finances:** Input your **Total Seasonal Budget (₹)** to anchor financial constraints for the upcoming stages.
4. **Advance:** Review the verified crop preview image and click **Start Land Preparation Guide** to proceed.

---

### Step 2: Stage 1 – Detailed Land Preparation

This phase focuses on creating an ideal soil bed environment before seeds are introduced.

1. **Log Parameters:** Use the slider to select the current ambient **Field Temperature (°C)** and pick your exact **Soil Profile** classification (Loamy, Clay, Sandy, Black Cotton, or Red Soil).
2. **Input Expenses:** Document your machinery rental and labor costs in the **Tractor & Labor Cost (₹)** field.
3. **Review Expert Recommendations:** Read the dynamically served advice. For example:
* Recommended field implements tailored to your crop variant (e.g., using a *Disc Plow* followed by a *Leveler*).
* Suggested organic material load (e.g., applying 10 tons of Farm Yard Manure per acre).
* High-heat warnings: If your logged temperature exceeds 30°C, the system advises incorporating green manure to protect soil moisture retention.



---

### Step 3: Stage 2 – Sowing & Seed Treatment

This stage establishes correct field spatial geometry and biological protections for the seed embryos.

1. **Select Sowing Strategy:** Choose your planting method (Direct Sowing, Transplanting, or Drilling).
2. **Declare Seed Source:** Toggle your source material between *Certified Govt Seeds*, *Private Hybrid*, or *Saved Seed*.
3. **Log Sowing Expenses:** Record your combined **Seed & Labor Cost (₹)**.
4. **Review Safety Checklist:** * **Treatment Advice:** Implements rules reminding you to treat seeds with biological agents (like *Trichoderma* at 10g/kg) to eliminate root-rot and fungal pathogens.
* **Spacing Geometry:** Displays the optimal centimeter-by-centimeter layout spacing for your specific crop choice to eliminate root overcrowding.
* **Germination Warnings:** If you selected *Saved Seed*, a warning highlights the risks of hollow seeds and recommends a salt-water float verification test.



---

### Step 4: Stage 3 – Nutrition & Irrigation Management

This phase tracks resource delivery during the active vegetative growth period.

1. **Configure Water Systems:** Choose your delivery infrastructure (Drip Irrigation, Sprinkler, or Flood Irrigation).
2. **Build a Fertilization Plan:** Select specific target macronutrients and micronutrients from the checklist (Urea, DAP, Potash, Zinc Sulfate, Boron).
3. **Log Operational Overhead:** Record your cumulative **Irrigation & Fertilizer Cost (₹)**.
4. **Deploy AI Growth Guides:** * The app reads the master database to remind you of your variant's inherent water demand profile.
* **Split-Dosing Rules:** If *Urea* is selected, an explicit breakdown guides you to split applications into three timeline intervals (Sowing, 30 days post-sowing, and Flowering) to avoid nitrogen leaching.
* **Pest Controls:** Prompts you with target early-stage insects to watch out for (e.g., Aphids and Jassids).



---

### Step 5: Stage 4 – Harvest & Post-Harvest Storage

This step ensures you preserve crop quality and avoid structural loss during storage.

1. **Set Moisture Thresholds:** Use the slider to input your targeted or tested **Grain/Fruit Moisture Percentage (%)**.
2. **Log Harvest Expenses:** Track your field clearing and logistics costs in the **Harvest & Transport Cost (₹)** field.
3. **Review Storage Protocols:**
* **Curing Indicators:** Displays specific processing tips, such as leaving root or onion crops in the open field for 3 days to properly harden skins before bagging.
* **Mold Prevention Rules:** If your moisture input exceeds 14%, the app triggers an active error notification, warning you that high moisture levels generate catastrophic storage mold and requiring you to dry the crop further.
* **Packaging Strategy:** Outlines explicit container types (e.g., perforated crates for ventilation-dependent fruits vs. breathable jute bags for grains).



---

### Step 6: Stage 5 – Market Optimization & Project Completion

The final phase handles the financial accounting and wholesale price modeling of your agricultural project.

1. **Input Mandi Valuations:** Review current trade metrics and input the baseline **Mandi Price** matching your category's unit layout (e.g., per *kg*, *quintal*, *ton*, or *bundle*).
2. **Calculate True Overhead:** Input your local clearing charges, cleaning labor, and packaging fees in the **Total Overhead per Unit (₹)** container.
3. **Define Desired Margin:** Type in the exact **Profit Margin per Unit (₹)** you intend to clear.
4. **Quantify Total Yield:** Input the total physical mass of your **Harvested Quantity**.
5. **Evaluate Business Summary:** The analytics dashboard processes your inputs and produces real-time financial metrics:
* **Suggested Sale Price:** Automatically calculates `Mandi Price + Overhead + Desired Profit` to establish your ideal wholesale price tag.
* **Total Projected Revenue:** Multiplies your suggested price against total quantity to display your macro financial generation for the season.


6. **Cycle Completion:** Click the **Complete & Reset Project** button. This safely wipes the temporary session memory and loops you back to Stage 1, completely fresh for your next seasonal crop selection.
7. 
