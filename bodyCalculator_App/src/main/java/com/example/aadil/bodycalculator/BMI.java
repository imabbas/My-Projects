package com.example.aadil.bodycalculator;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.math.BigDecimal;
import java.math.MathContext;

public class BMI extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bmi);

        Button calcbtn = (Button) findViewById(R.id.calcbtn);
        Button menubtn = (Button) findViewById(R.id.bmiMenu);

        assert calcbtn != null;
        calcbtn.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                EditText e1 = (EditText)findViewById(R.id.editText2);
                assert e1 != null;
                EditText e2 = (EditText)findViewById(R.id.editText3);
                assert e2 != null;
                TextView t1 = (TextView)findViewById(R.id.theResult);
                assert t1 != null;
                double height = Integer.parseInt(e2.getText().toString());
                double weight = Integer.parseInt(e1.getText().toString());
                t1.setText(Double.toString(bodyMassIndex(weight, height)));
//                startActivity(new Intent(BMI.this,BMI_Display.class ));
            }
        });

        assert menubtn != null;
        menubtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(BMI.this, MainActivity.class));
            }
        });



    }

    public static double bodyMassIndex(double yourWeight, double yourHeight) {
        double bmi;
        yourWeight = yourWeight * (0.453592);
        yourHeight = yourHeight * (0.0254);
        yourHeight = (yourHeight*yourHeight);
        bmi = yourWeight/yourHeight;
        BigDecimal bd = new BigDecimal(bmi);
        bd = bd.round(new MathContext(2));
        bmi = bd.doubleValue();


        return bmi;
    }


}
