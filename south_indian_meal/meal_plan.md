content = """# 6-Week South Indian Vegetarian Weight-Loss Meal Plan Request

I am a software professional who works more than 8 hours per day and leads a mostly sedentary lifestyle.

I am looking for a **healthy, vegetarian, South Indian meal plan for weight loss**, organized as a **7-day weekly diet chart repeated with variety across 6 weeks**.

## Requirements

Please create a **6-week vegetarian South Indian diet plan**, with each week containing a complete **7-day meal schedule**.

For every day, include:

- **Breakfast**
- **Mid-morning snack**
- **Lunch**
- **Evening snack**
- **Dinner**
- **Approximate calories for each meal**
- **Approximate total daily calories**

## Meal Preferences

The meals should be simple, familiar South Indian foods such as:

- Idli
- Dosa
- Upma
- Pongal
- Oats or millet-based breakfast
- Rice with vegetables, sambar, rasam, kootu, poriyal, or curd for lunch
- Chapati with vegetables, dal, paneer, or light curry for dinner
- Fruits, buttermilk, nuts, sprouts, sundal, or similar healthy snacks

## Important Conditions

1. The diet must be **100% vegetarian**.
2. The meals should support **healthy and sustainable weight loss**.
3. Ingredients should be **easily available in regular Indian or U.S. grocery stores**.
4. The entire day's meals should be possible to prepare with approximately **1 hour of total cooking/preparation time per day**.
5. Use **simple recipes with minimal ingredients and minimal cleanup**.
6. Prefer meals that can be **batch-prepared or reused between breakfast, lunch, and dinner** where practical.
7. Avoid excessive oil, sugar, deep-fried foods, sweets, and highly processed foods.
8. Include adequate **protein, fiber, vegetables, and healthy fats**.
9. Keep meals practical for someone working long hours at a desk.
10. Avoid complicated recipes that require several hours of cooking.

## Format Requested

Please present the plan in a table for each week using columns similar to:

| Day | Breakfast | Mid-Morning Snack | Lunch | Evening Snack | Dinner | Approx. Daily Calories |
|---|---|---|---|---|---|---|

For every meal, mention the **portion size and approximate calories**.

Example:

| Meal | Example |
|---|---|
| Breakfast | 3 idlis + 1 cup sambar — approximately 350 calories |
| Mid-Morning Snack | 1 apple + 5 almonds — approximately 130 calories |
| Lunch | 1 cup cooked rice + sambar + vegetable poriyal + curd — approximately 500 calories |
| Evening Snack | Buttermilk + roasted chana — approximately 150 calories |
| Dinner | 2 chapatis + mixed vegetable curry + dal — approximately 400 calories |

## Additional Information Requested

After the 6-week plan, also provide:

- A **weekly grocery shopping list**
- A **basic Sunday meal-preparation plan**
- Foods that can be prepared in advance
- Recommended portion-control guidelines
- Easy ingredient substitutions
- Tips to manage hunger while working long hours
- Suggestions for reducing rice portions gradually without completely eliminating South Indian foods
- High-protein vegetarian options that can be incorporated into South Indian meals
- Guidance on drinking water, tea, and coffee during the day

The final meal plan should be **realistic, affordable, easy to follow, nutritionally balanced, and sustainable for long-term weight loss**.
"""

path = "/mnt/data/south_indian_vegetarian_6_week_meal_plan_prompt.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(path)
