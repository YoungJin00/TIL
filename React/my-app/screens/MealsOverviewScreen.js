import { View, FlatList, StyleSheet} from 'react-native'
import { MEALS } from '../data/dummy-data'
import MealItem from '../components/MealItem'

function MealsOverviewScreen({ route }) {
    const catId = route.params.categoryId

    const displayedMeals = MEALS.filter((meal) => {
        return meal.categoryIds.indexOf(catId) >= 0
    })
    function renderMealItem(itemData) {
        const item = itemData.item
        const MealProps = {
            title: item.title,
            imgUrl: item.imageUrl,
            duration: item.duration,
            complexity: item.complexity,
            affordability: item.affordability
        }
        return <MealItem {...MealProps} />
    }
    return (
        <View style={style.container}>
            <FlatList data={displayedMeals} keyExtractor={(item) => item.id} renderItem={renderMealItem}/>
        </View>
    )

}

export default MealsOverviewScreen

const style = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16
    }
})