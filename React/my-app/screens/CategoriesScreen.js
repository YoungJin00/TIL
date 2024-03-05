import { FlatList } from "react-native";
import { CATEGORIES } from "../data/dummy-data";
import CategoryGridTile from "../components/CategoryGridTile";





function CategoriesScreen({navigation}) {

  function renderCategoryItem(itemData) {
    
    function handleOnPress() {
      navigation.navigate('MealsOverview', {
        categoryId: itemData.item.id,
      });
    }
    return (
      <CategoryGridTile title={itemData.item.title} color={itemData.item.color} onPress={handleOnPress} />
    );
  }
  return (
    <FlatList
      data={CATEGORIES}
      keyExtractor={(item) => item.id}
      renderItem={renderCategoryItem}
      numColumns={2}
    />
  );
}

export default CategoriesScreen;
