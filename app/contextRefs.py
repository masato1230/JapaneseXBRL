"""
contextRef is the item that corresponds to the type of value in the xbrl file.
"""

contextRefs = (
    # ContextRef for Basic information: Such as Company name, fiscal year start.
    'FilingDateInstant',

    # ContextRefs corresponding to the item in the consolidated income statement
    'CurrentYearDuration',
    'Prior1YearDuration',
    'Prior2YearDuration',
    'Prior3YearDuration',
    'Prior4YearDuration',

    # ContextRefs corresponding to the consolidated balance sheet item
    'CurrentYearInstant',
    'Prior1YearInstant',
    'Prior2YearInstant',
    'Prior3YearInstant',
    'Prior4YearInstant',
    # - capital stock member
    'CurrentYearInstant_CapitalStockMember',
    'Prior1YearInstant_CapitalStockMember',
    'Prior3YearInstant_CapitalStockMember'
    # - capital member
    'CurrentYearInstant_CapitalSurplusMember',
    'Prior1YearInstant_CapitalSurplusMember',
    'Prior2YearInstant_CapitalSurplusMember',
    # - retained earnings member
    'CurrentYearInstant_RetainedEarningsMember',
    'Prior1YearInstant_RetainedEarningsMember',
    'Prior2YearInstant_RetainedEarningsMember'
    # - treasury stock member
    'CurrentYearInstant_TreasuryStockMember',
    'Prior1YearInstant_TreasuryStockMember',
    'Prior2YearInstant_TreasuryStockMember',
    # - shareholders equity member
    'CurrentYearInstant_ShareholdersEquityMember',
    'Prior1YearInstant_ShareholdersEquityMember',
    'Prior2YearInstant_ShareholdersEquityMember',
    # - valuation difference on available for sales securities member
    'CurrentYearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember',
    'Prior1YearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember',
    'Prior2YearInstant_ValuationDifferenceOnAvailableForSaleSecuritiesMember',
    # - foreign currency translation adjustment member
    'CurrentYearInstant_ForeignCurrencyTranslationAdjustmentMember',
    'Prior1YearInstant_ForeignCurrencyTranslationAdjustmentMember',
    'Prior2YearInstant_ForeignCurrencyTranslationAdjustmentMember',
    # - remeasurements of defined benefit plans member
    'CurrentYearInstant_RemeasurementsOfDefinedBenefitPlansMember',
    'Prior1YearInstant_RemeasurementsOfDefinedBenefitPlansMember',
    'Prior2YearInstant_RemeasurementsOfDefinedBenefitPlansMember',
    # -valuation and translation adjustments member
    'CurrentYearInstant_ValuationAndTranslationAdjustmentsMember',
    'Prior1YearInstant_ValuationAndTranslationAdjustmentsMember',
    'Prior2YearInstant_ValuationAndTranslationAdjustmentsMember',
    # - non controlling interests member
    'CurrentYearInstant_NonControllingInterestsMember',
    'Prior1YearInstant_NonControllingInterestsMember',
    'Prior2YearInstant_NonControllingInterestsMember',

    # ContextRefs coresponding to the item in nonconsolidated income statements
    'CurrentYearDuration_NonConsolidatedMember',
    'Prior1YearDuration_NonConsolidatedMember',
    'Prior2YearDuration_NonConsolidatedMember',
    'Prior3YearDuration_NonConsolidatedMember',
    'Prior4YearDuration_NonConsolidatedMember',

    # ContextRefs corresponding to the non consolidated balance sheet item
    'CurrentYearInstant_NonConsolidatedMember',
    'Prior1YearInstant_NonConsolidatedMember',
    'Prior2YearInstant_NonConsolidatedMember',
    'Prior3YearInstant_NonConsolidatedMember',
    'Prior4YearInstant_NonConsolidatedMember',
    # - capital stock member
    'CurrentYearInstant_NonConsolidatedMember_CapitalStockMember',
    'Prior1YearInstant_NonConsolidatedMember_CapitalStockMember',
    'Prior2YearInstant_NonConsolidatedMember_CapitalStockMember',
    # - legal capital surplus member
    'CurrentYearInstant_NonConsolidatedMember_LegalCapitalSurplusMember',
    'Prior1YearInstant_NonConsolidatedMember_LegalCapitalSurplusMember',
    'Prior2YearInstant_NonConsolidatedMember_LegalCapitalSurplusMember',
    # - legal retained earnings member
    'CurrentYearInstant_NonConsolidatedMember_LegalRetainedEarningsMember',
    'Prior1YearInstant_NonConsolidatedMember_LegalRetainedEarningsMember',
    'Prior2YearInstant_NonConsolidatedMember_LegalRetainedEarningsMember',
    # - reserve for reduction entry of replaced property member
    'CurrentYearInstant_NonConsolidatedMember_ReserveForReductionEntryOfReplacedPropertyMember',
    'Prior1YearInstant_NonConsolidatedMember_ReserveForReductionEntryOfReplacedPropertyMember',
    'Prior2YearInstant_NonConsolidatedMember_ReserveForReductionEntryOfReplacedPropertyMember',
    # - general reserve member
    'CurrentYearInstant_NonConsolidatedMember_GeneralReserveMember',
    'Prior1YearInstant_NonConsolidatedMember_GeneralReserveMember',
    'Prior2YearInstant_NonConsolidatedMember_GeneralReserveMember',
    # - retained earnings brought forward member
    'CurrentYearInstant_NonConsolidatedMember_GeneralReserveMember',
    'Prior1YearInstant_NonConsolidatedMember_GeneralReserveMember',
    'Prior2YearInstant_NonConsolidatedMember_GeneralReserveMember',
    # retained earnings member
    'CurrentYearInstant_NonConsolidatedMember_RetainedEarningsMember',
    'Prior1YearInstant_NonConsolidatedMember_RetainedEarningsMember',
    'Prior2YearInstant_NonConsolidatedMember_RetainedEarningsMember',
    # treasury stock member
    'CurrentYearInstant_NonConsolidatedMember_RetainedEarningsMember',
    'Prior1YearInstant_NonConsolidatedMember_RetainedEarningsMember',
    'Prior2YearInstant_NonConsolidatedMember_RetainedEarningsMember',
    # shareholders equity member
    'CurrentYearInstant_NonConsolidatedMember_RetainedEarningsMember',
    'Prior1YearInstant_NonConsolidatedMember_RetainedEarningsMember',
    'Prior2YearInstant_NonConsolidatedMember_RetainedEarningsMember',
    # valuation differene on available for sale securities member
    'CurrentYearInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember',
    'Prior1YearInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember',
    'Prior2YearInstant_NonConsolidatedMember_ValuationDifferenceOnAvailableForSaleSecuritiesMember',

    # ContextRefs corresponding to the shareholder statemet
    'CurrentYearInstant_No1MajorShareholdersMember',
    'CurrentYearInstant_No2MajorShareholdersMember',
    'CurrentYearInstant_No3MajorShareholdersMember',
    'CurrentYearInstant_No4MajorShareholdersMember',
    'CurrentYearInstant_No5MajorShareholdersMember',
    'CurrentYearInstant_No6MajorShareholdersMember',
    'CurrentYearInstant_No7MajorShareholdersMember',
    'CurrentYearInstant_No8MajorShareholdersMember',
    'CurrentYearInstant_No9MajorShareholdersMember',
    'CurrentYearInstant_No10MajorShareholdersMember',
)
