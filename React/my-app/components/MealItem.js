import { View, Text, Image, Pressable, StyleSheet } from "react-native";

function MealItem({ title, imgUrl, duration, complexity, affordability
 }) {
  return (
    <View style={style.mealItem}>
      <Pressable >
        <Text style={style.text}>{title}</Text>
        <Image source={{uri: imgUrl}} style={style.image} />
        <View>
          <Text>{duration} m</Text>
          <Text>{complexity.toUpperCase()}</Text>
          <Text>{affordability.toUpperCase()}</Text>
        </View>
      </Pressable>
    </View>
  );
}

export default MealItem;


const style = StyleSheet.create({
    mealItem: {
        margin: 16,
        borderRadius: 8,
        overflow: 'hidden',
        backgroundColor: 'white',

    },
    image: {
        width: '100%',
        height: 200,
    },
    text: {
        textAlign: 'center',
        fontWeight: 'bold',
        fontSize: 18
    }
})