# importy
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import LabelEncoder

# wczytywanie datasetu
dataset_path = r"C:\Users\Iksem\OneDrive\Desktop\python selekcja cech\Student_performance_data _.csv"
data = pd.read_csv(dataset_path)

# print(data.head(20))  # pierwsze 20 rekordow

# tu kolumna na ktora te inne maja miec obliczony wplyw (no ta docelowa wiadomo o co chodzi)
target_column = 'GradeClass'

# podzielenie na zmienne cech (X) i zmienną docelową (y)
X = data.drop(columns=[target_column, 'StudentID'])  # Usunięcie kolumny StudentID
y = data[target_column]

# tutaj zamiast np kobieta mezczyzna jest 0 1 
for column in X.columns:
    if X[column].dtype == 'object':
        le = LabelEncoder()
        X[column] = le.fit_transform(X[column])

# dane treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# uzycie SelectKBest by wybral k najlepszych cech
k = 3  # k to liczba cech jaka wybierze
selector = SelectKBest(score_func=f_classif, k=k)  # f_classif dla klasyfikacji (komentarz od chatu giepeti nie wiem o co chodzi)
selector.fit(X_train, y_train)

# jakas maska wybranych cech nie wiem co to dokladnie robi
selected_features_mask = selector.get_support()

# wyswietlanie nazw wybranych cech
selected_features = X.columns[selected_features_mask]
print("Wybrane cechy:", selected_features.tolist())

# selekcja cech na danych treningowych i testowych
X_train_selected = selector.transform(X_train)
X_test_selected = selector.transform(X_test)

print(f"Liczba wybranych cech: {X_train_selected.shape[1]}")

# trenowanie modelu na wybranych cechach
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_selected, y_train)
accuracy = model.score(X_test_selected, y_test)

print(f"Dokładność modelu na wyselekcjonowanych cechach: {accuracy * 100:.2f}%")

# tutaj porownanie jak myslalo ai ze bedzie a jak jest w rzeczywistoci

# y_pred = model.predict(X_test_selected)
# predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
# print(predictions_df)