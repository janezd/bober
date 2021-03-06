<?php

/**
 * This is the model class for table "school_category".
 *
 * The followings are the available columns in table 'school_category':
 * @property integer $id
 * @property string $name
 * @property integer $active
 *
 * The followings are the available model relations:
 * @property School[] $schools
 */
class SchoolCategory extends CActiveRecord {

    /**
     * Returns the static model of the specified AR class.
     * @param string $className active record class name.
     * @return SchoolCategory the static model class
     */
    public static function model($className = __CLASS__) {
        return parent::model($className);
    }

    /**
     * @return string the associated database table name
     */
    public function tableName() {
        return 'school_category';
    }

    /**
     * @return array validation rules for model attributes.
     */
    public function rules() {
        // NOTE: you should only define rules for those attributes that
        // will receive user inputs.
        return array(
            array('name', 'required'),
            array('active', 'numerical', 'integerOnly' => true),
            array('name', 'length', 'max' => 255),
            // The following rule is used by search().
            // Please remove those attributes that should not be searched.
            array('id, name, active', 'safe', 'on' => 'search'),
        );
    }

    /**
     * @return array relational rules.
     */
    public function relations() {
        // NOTE: you may need to adjust the relation name and the related
        // class name for the relations automatically generated below.
        return array(
            'schools' => array(self::HAS_MANY, 'School', 'school_category_id'),
        );
    }

    /**
     * @return array customized attribute labels (name=>label)
     */
    public function attributeLabels() {
        return array(
            'id' => Yii::t('app', 'id'),
            'name' => Yii::t('app', 'name'),
            'active' => Yii::t('app', 'active'),
        );
    }

    public function getCanView() {
        return $this->CanView();
    }

    public function CanView() {
        $user = User::model()->find('id=:id', array(':id' => Yii::app()->user->id));
        $superuser = $user != null ? $user->superuser : 0;
        if ($superuser == 1 || $user->profile->user_role >= 10) {
            return true;
        }
        return false;
    }

    public function getCanUpdate() {
        return $this->CanUpdate();
    }

    public function CanUpdate() {
        return $this->CanView();
    }

    public function getCanDelete() {
        return $this->CanDelete();
    }

    public function CanDelete() {
        return $this->CanView();
    }

    /**
     * Retrieves a list of models based on the current search/filter conditions.
     * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
     */
    public function search($show_all = false) {
        // Warning: Please modify the following code to remove attributes that
        // should not be searched.

        $criteria = new CDbCriteria;

        $criteria->compare('id', $this->id);
        $criteria->compare('name', $this->name, true);
        $criteria->compare('active', $this->active);

        $pagination = true;
        if ($show_all) {
            $pagination = false;
        }
        
        $options = array('criteria' => $criteria);
        
        if($pagination == false){
            $options['pagination'] = false;
        }
        
        return new CActiveDataProvider($this,$options);
    }

}