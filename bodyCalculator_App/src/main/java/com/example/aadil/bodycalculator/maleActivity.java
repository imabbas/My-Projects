package com.example.aadil.bodycalculator;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class maleActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_male);

        Button calcbtn = (Button) findViewById(R.id.maleCalc);
        Button menubtn = (Button) findViewById(R.id.mMenu);

        assert calcbtn != null;
        calcbtn.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                EditText e1 = (EditText)findViewById(R.id.editText4);
                assert e1 != null;
                EditText e2 = (EditText)findViewById(R.id.editText5);
                assert e2 != null;
                TextView t1 = (TextView)findViewById(R.id.maleResult);
                assert t1 != null;
                double weight = Integer.parseInt(e1.getText().toString());
                double waist = Integer.parseInt(e2.getText().toString());
                t1.setText(Double.toString(maleFat(weight, waist)) + "%");
//                startActivity(new Intent(BMI.this,BMI_Display.class ));
            }
        });

        assert menubtn != null;
        menubtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(maleActivity.this, MainActivity.class));
            }
        });




    }

    public static double maleFat(double yourWeight, double yourWaist) {

        double weight2;
        double leanBodyMass;
        double bodyFatWeight;
        double bodyFatPercentage;

        weight2 = (yourWeight * 1.082) + 94.42;
        yourWaist = yourWaist * 4.15;

        leanBodyMass = weight2 - yourWaist;
        bodyFatWeight = yourWeight - leanBodyMass;
        bodyFatPercentage = (bodyFatWeight * 100)/yourWeight;
        BigDecimal bd = new BigDecimal(bodyFatPercentage);
        bd = bd.setScale(1, RoundingMode.HALF_UP);
        bodyFatPercentage = bd.doubleValue();

        return bodyFatPercentage;

    }
}
