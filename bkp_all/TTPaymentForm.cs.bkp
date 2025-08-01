using Infragistics.Win;
using Infragistics.Win.FormattedLinkLabel;
using Infragistics.Win.UltraWinGrid;
using Infragistics.Win.UltraWinTabControl;
using Micromind.ClientLibraries;
using Micromind.ClientUI.Libraries;
using Micromind.ClientUI.Properties;
using Micromind.ClientUI.WindowsForms.DataEntries.Customers;
using Micromind.ClientUI.WindowsForms.DataEntries.Others;
using Micromind.Common;
using Micromind.Common.Data;
using Micromind.Common.Interfaces;
using Micromind.DataControls;
using Micromind.UISupport;
using System;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Windows.Forms;

namespace Micromind.ClientUI.WindowsForms.DataEntries.Accounts
{
	public class TTPaymentForm : Form, IForm, IWorkFlowForm
	{
		private string requestSysDocID = "";

		private TransactionData currentData;

		private const string TABLENAME_CONST = "GL_Transaction";

		private const string IDFIELD_CONST = "VoucherID";

		private bool isNewRecord = true;

		private bool useJobCosting = CompanyPreferences.UseJobCosting;

		private bool isCostCenterMandatory = CompanyPreferences.IsCostCenterMandatory;

		private bool showAllocationForm = CompanyPreferences.ShowAllocationForm;

		private ScreenAccessRight screenRight;

		private bool ShowSupplierBal;

		private bool ShowCustomerBal;

		private bool ShowAccountBal;

		private bool ShowEmployeeBal;

		private bool AllowEditTransaction;

		private bool AllowEditTransDiffLocation;

		private bool isVoid;

		private IContainer components;

		private ToolStrip toolStrip1;

		private Panel panelButtons;

		private Line linePanelDown;

		private XPButton xpButton1;

		private XPButton buttonSave;

		private ToolStripButton toolStripButtonFirst;

		private ToolStripButton toolStripButtonPrevious;

		private ToolStripButton toolStripButtonNext;

		private ToolStripButton toolStripButtonLast;

		private ToolStripSeparator toolStripSeparator1;

		private ToolStripButton toolStripButtonFind;

		private ToolStripTextBox toolStripTextBoxFind;

		private ToolStripSeparator toolStripSeparator2;

		private FormManager formManager;

		private TextBox textBoxVoucherNumber;

		private Label label1;

		private MMLabel mmLabel1;

		private TextBox textBoxRef1;

		private TextBox textBoxNote;

		private Label label3;

		private CurrencySelector currencySelector;

		private UltraFormattedLinkLabel labelCurrency;

		private AnalysisComboBox comboBoxAnalysis;

		private XPButton buttonDelete;

		private XPButton buttonNew;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel2;

		private XPButton buttonVoid;

		private Label labelVoided;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel3;

		private PayeeSelector payeeSelector1;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel4;

		private CostCenterComboBox comboBoxCostCenter;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel5;

		private SysDocComboBox comboBoxSysDoc;

		private TextBox textBoxPayeeName;

		private Label labelAnalysis;

		private flatDatePicker dateTimePickerDate;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel6;

		private AmountTextBox textBoxAmount;

		private TextBox textBoxDescription;

		private Label label4;

		private Panel panelDetails;

		private ToolStripButton toolStripButtonPrint;

		private ToolStripButton toolStripButtonPreview;

		private TextBox textBoxBalance;

		private Label label5;

		private Label label2;

		private TextBox textBoxRegBalance;

		private ToolStripSeparator toolStripSeparator3;

		private ToolStripButton toolStripButtonOpenList;

		private ToolStripDropDownButton toolStripDropDownButton1;

		private ToolStripMenuItem saveAsDraftToolStripMenuItem;

		private ToolStripMenuItem loadDraftToolStripMenuItem;

		private TextBox textBox1;

		private BankAccountsComboBox comboBoxBankAccount;

		private ToolStripButton toolStripButtonAttach;

		private ToolStripSeparator toolStripSeparator4;

		private ToolStripSeparator toolStripSeparator5;

		private ToolStripButton toolStripButtonDistribution;

		private UltraTabControl ultraTabControl1;

		private UltraTabSharedControlsPage ultraTabSharedControlsPage1;

		private UltraTabPageControl tabPageItems;

		private UltraTabPageControl tabPageExpense;

		private DataEntryGrid dataGridExpense;

		private NumberTextBox textBoxTotalExpense;

		private Label label8;

		private ExpenseCodeComboBox comboBoxGridExpenseCode;

		private CurrencyComboBox comboBoxGridCurrency;

		private Line line1;

		private Label labelBaseCurrency;

		private AmountTextBox textBoxTotalAmount;

		private MMLabel mmLabel5;

		private AmountTextBox textBoxAmountBase;

		private AmountTextBox textBoxTotalFees;

		private MMLabel mmLabel4;

		private Label labelAmountBase;

		private ToolStripButton toolStripButtonApproval;

		private ToolStripLabel toolStripLabelApproval;

		private ToolStripSeparator toolStripSeparatorApproval;

		private XPButton buttonSelectRequest;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel1;

		private TextBox textBoxRequest;

		private ToolStripButton toolStripButtonInformation;

		private MMLabel mmLabel3;

		private AmountTextBox textBoxTotalDue;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel8;

		private XPButton buttonSelectInvoice;

		private UltraFormattedLinkLabel linkLabelTax;

		private AmountTextBox textBoxTaxAmount;

		private Panel panelJobCC;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel7;

		private JobComboBox comboBoxJob;

		private UltraFormattedLinkLabel ultraFormattedLinkLabel9;

		private CostCategoryComboBox comboBoxCostCategory;

		public ScreenAreas ScreenArea => ScreenAreas.Accounts;

		public int ScreenID => 1006;

		public ScreenTypes ScreenType => ScreenTypes.Transaction;

		private string SystemDocID => comboBoxSysDoc.SelectedID;

		private bool IsDirty
		{
			get
			{
				if (IsVoid)
				{
					return false;
				}
				return formManager.GetDirtyStatus();
			}
		}

		private bool IsNewRecord
		{
			get
			{
				return isNewRecord;
			}
			set
			{
				isNewRecord = value;
				bool enabled;
				if (value)
				{
					buttonNew.Text = UIMessages.ClearButtonText;
					XPButton xPButton = buttonDelete;
					enabled = (buttonVoid.Enabled = false);
					xPButton.Enabled = enabled;
					textBoxVoucherNumber.Enabled = true;
					comboBoxSysDoc.Enabled = true;
				}
				else
				{
					buttonNew.Text = UIMessages.NewButtonText;
					XPButton xPButton2 = buttonDelete;
					enabled = (buttonVoid.Enabled = true);
					xPButton2.Enabled = enabled;
					textBoxVoucherNumber.Enabled = false;
					comboBoxSysDoc.Enabled = false;
					buttonSelectInvoice.Enabled = false;
				}
				comboBoxSysDoc.Enabled = value;
				toolStripButtonAttach.Enabled = !value;
				toolStripButtonDistribution.Enabled = !value;
				if (!screenRight.New && isNewRecord)
				{
					buttonSave.Enabled = false;
					buttonVoid.Enabled = false;
				}
				else if (!screenRight.Edit && !isNewRecord)
				{
					buttonSave.Enabled = false;
					buttonVoid.Enabled = false;
				}
				else
				{
					buttonSave.Enabled = true;
				}
				if (!screenRight.Delete)
				{
					buttonDelete.Enabled = false;
				}
				ToolStripButton toolStripButton = toolStripButtonPrint;
				enabled = (toolStripButtonPreview.Enabled = !isNewRecord);
				toolStripButton.Enabled = enabled;
				SetApprovalStatus();
			}
		}

		private bool IsVoid
		{
			get
			{
				return isVoid;
			}
			set
			{
				if (isVoid != value)
				{
					isVoid = value;
					buttonSave.Enabled = !value;
					panelDetails.Enabled = !value;
					labelVoided.Visible = value;
					if (value)
					{
						buttonVoid.Text = UIMessages.Unvoid;
					}
					else
					{
						buttonVoid.Text = UIMessages.Void;
					}
				}
			}
		}

		public TTPaymentForm()
		{
			InitializeComponent();
			comboBoxGridExpenseCode.ExpenseCodeType = ExpenseCodeTypes.BankFee;
			if (useJobCosting)
			{
				panelJobCC.Visible = true;
			}
			AddEvents();
		}

		private void AddEvents()
		{
			base.Load += TransactionLeavesForm_Load;
			comboBoxSysDoc.SelectedIndexChanged += comboBoxSysDoc_SelectedIndexChanged;
			comboBoxCostCenter.SelectedIndexChanged += comboBoxCostCenter_SelectedIndexChanged;
			payeeSelector1.SelectedItemChanged += payeeSelector1_SelectedItemChanged;
			comboBoxBankAccount.SelectedIndexChanged += comboBoxBankAccount_SelectedIndexChanged;
			base.KeyDown += Form_KeyDown;
			comboBoxBankAccount.DescriptionTextBox = textBox1;
			dataGridExpense.AfterCellUpdate += dataGridExpense_AfterCellUpdate;
			textBoxTotalFees.TextChanged += textBoxTotalFees_TextChanged;
			textBoxAmount.TextChanged += textBoxAmount_TextChanged;
			currencySelector.CurrencyRateChanged += currencySelector_CurrencyRateChanged;
			currencySelector.SelectedIndexChanged += currencySelector_SelectedIndexChanged;
			dataGridExpense.HeaderClicked += dataGridItems_HeaderClicked;
		}

		private void currencySelector_SelectedIndexChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void currencySelector_CurrencyRateChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void textBoxTotalFees_TextChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void dataGridItems_HeaderClicked(object sender, EventArgs e)
		{
			UltraGridColumn ultraGridColumn = sender as UltraGridColumn;
			if (dataGridExpense.ActiveRow != null && ultraGridColumn.Key == "Tax" && dataGridExpense.ActiveRow != null)
			{
				TaxTransactionData taxData = new TaxTransactionData();
				if (dataGridExpense.ActiveRow.Cells["Tax"].Tag != null)
				{
					taxData = (dataGridExpense.ActiveRow.Cells["Tax"].Tag as TaxTransactionData);
				}
				TaxDistibutionDialog taxDistibutionDialog = new TaxDistibutionDialog();
				taxDistibutionDialog.TaxData = taxData;
				taxDistibutionDialog.ShowDialog();
			}
		}

		private void textBoxAmount_TextChanged(object sender, EventArgs e)
		{
			CalculateBaseAmount();
		}

		private void dataGridExpense_AfterCellUpdate(object sender, CellEventArgs e)
		{
			try
			{
				if (dataGridExpense.ActiveRow != null)
				{
					if (e.Cell.Column.Key == "FeeCode")
					{
						dataGridExpense.ActiveRow.Cells["Description"].Value = comboBoxGridExpenseCode.SelectedName;
						dataGridExpense.ActiveRow.Cells["ExpenseAccountID"].Value = comboBoxGridExpenseCode.AccountID;
						if (dataGridExpense.ActiveRow.Cells["Currency"].Value.ToString() == "")
						{
							dataGridExpense.ActiveRow.Cells["Currency"].Value = Global.BaseCurrencyID;
						}
						ItemTaxOptions taxOption = comboBoxGridExpenseCode.TaxOption;
						dataGridExpense.ActiveRow.Cells["TaxOption"].Value = taxOption;
						switch (taxOption)
						{
						case ItemTaxOptions.Taxable:
							dataGridExpense.ActiveRow.Cells["TaxGroupID"].Value = comboBoxGridExpenseCode.TaxGroupID;
							break;
						case ItemTaxOptions.NonTaxable:
							dataGridExpense.ActiveRow.Cells["TaxGroupID"].Value = DBNull.Value;
							break;
						}
					}
					else if (e.Cell.Column.Key == "TaxGroupID")
					{
						ItemTaxOptions itemTaxOption = ItemTaxOptions.NonTaxable;
						if (!e.Cell.Row.Cells["TaxOption"].Value.IsNullOrEmpty())
						{
							itemTaxOption = (ItemTaxOptions)byte.Parse(e.Cell.Row.Cells["TaxOption"].Value.ToString());
						}
						TaxTransactionData tag = TaxHelper.CreateTaxDetailData(PayeeTaxOptions.Taxable, comboBoxGridExpenseCode.TaxGroupID, itemTaxOption, comboBoxGridExpenseCode.TaxGroupID);
						e.Cell.Row.Cells["Tax"].Tag = tag;
					}
					if (e.Cell.Column.Key == "Currency")
					{
						dataGridExpense.ActiveRow.Cells["Rate"].Value = comboBoxGridCurrency.SelectedRate.ToString();
						dataGridExpense.ActiveRow.Cells["RateType"].Value = comboBoxGridCurrency.SelectedRateType;
					}
					if (e.Cell.Column.Key == "Amount" || e.Cell.Column.Key == "Rate" || e.Cell.Column.Key == "Currency")
					{
						decimal result = default(decimal);
						decimal.TryParse(e.Cell.Value.ToString(), out result);
						UIGlobal.CalculateRowTax(e.Cell.Row, "Tax", result, default(decimal), default(decimal));
						SetRowLCAmount(dataGridExpense.ActiveRow);
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void comboBoxBankAccount_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (comboBoxBankAccount.SelectedID == "")
			{
				textBoxRegBalance.Clear();
				return;
			}
			decimal accountBalance = Factory.CompanyAccountSystem.GetAccountBalance(comboBoxBankAccount.SelectedID, includeOD: true);
			textBoxRegBalance.Text = accountBalance.ToString(Format.TotalAmountFormat, CultureInfo.CurrentCulture);
		}

		private void Form_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.Control && e.KeyCode == Keys.P && !IsNewRecord)
			{
				Print(isPrint: true, showPrintDialog: true, saveChanges: true);
			}
		}

		private void CalculateBaseAmount()
		{
			if (currencySelector.IsBaseCurrency)
			{
				textBoxAmountBase.Text = textBoxAmount.Text;
			}
			else
			{
				decimal result = default(decimal);
				decimal.TryParse(textBoxAmount.Text, out result);
				textBoxAmountBase.Text = currencySelector.GetBaseEquivalant(result).ToString(Format.TotalAmountFormat);
			}
			decimal result2 = default(decimal);
			decimal result3 = default(decimal);
			decimal.TryParse(textBoxAmountBase.Text, out result2);
			decimal.TryParse(textBoxTotalFees.Text, out result3);
			textBoxTotalAmount.Text = (result2 + result3).ToString();
		}

		private void SetupExpenseGrid()
		{
			dataGridExpense.SetupUI();
			dataGridExpense.DisplayLayout.Bands[0].Columns.ClearUnbound();
			DataTable dataTable = new DataTable();
			dataTable.Columns.Add("FeeCode");
			dataTable.Columns.Add("Description");
			dataTable.Columns.Add("ExpenseAccountID");
			dataTable.Columns.Add("Ref");
			dataTable.Columns.Add("Currency");
			dataTable.Columns.Add("TaxGroupID");
			dataTable.Columns.Add("TaxOption", typeof(byte));
			dataTable.Columns.Add("Tax", typeof(decimal));
			dataTable.Columns.Add("RateType");
			dataTable.Columns.Add("Rate", typeof(decimal));
			dataTable.Columns.Add("Amount", typeof(decimal));
			dataTable.Columns.Add("AmountLC", typeof(decimal));
			dataGridExpense.DataSource = dataTable;
			dataGridExpense.DisplayLayout.Bands[0].Columns["RateType"].Hidden = true;
			dataGridExpense.DisplayLayout.Bands[0].Columns["FeeCode"].CharacterCasing = CharacterCasing.Upper;
			dataGridExpense.DisplayLayout.Bands[0].Columns["FeeCode"].Header.Caption = "Fee Code";
			dataGridExpense.DisplayLayout.Bands[0].Columns["FeeCode"].MaxLength = 64;
			dataGridExpense.DisplayLayout.Bands[0].Columns["FeeCode"].InvalidValueBehavior = InvalidValueBehavior.RetainValueAndFocus;
			dataGridExpense.DisplayLayout.Bands[0].Columns["FeeCode"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
			dataGridExpense.DisplayLayout.Bands[0].Columns["FeeCode"].ValueList = comboBoxGridExpenseCode;
			dataGridExpense.DisplayLayout.Bands[0].Columns["ExpenseAccountID"].Hidden = true;
			dataGridExpense.DisplayLayout.Bands[0].Columns["ExpenseAccountID"].ExcludeFromColumnChooser = ExcludeFromColumnChooser.True;
			dataGridExpense.DisplayLayout.Bands[0].Columns["AmountLC"].Header.Caption = "Amount (" + Global.BaseCurrencyID + ")";
			dataGridExpense.DisplayLayout.Bands[0].Columns["AmountLC"].CellActivation = Activation.Disabled;
			dataGridExpense.DisplayLayout.Bands[0].Columns["AmountLC"].CellAppearance.TextHAlign = HAlign.Right;
			dataGridExpense.DisplayLayout.Bands[0].Columns["AmountLC"].CellAppearance.BackColorDisabled = Color.WhiteSmoke;
			dataGridExpense.DisplayLayout.Bands[0].Columns["AmountLC"].CellAppearance.ForeColorDisabled = Color.Black;
			dataGridExpense.DisplayLayout.Bands[0].Columns["AmountLC"].Format = Format.GridAmountFormat;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Currency"].Style = Infragistics.Win.UltraWinGrid.ColumnStyle.DropDownValidate;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Currency"].ValueList = comboBoxGridCurrency;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Description"].MaxLength = 64;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Ref"].MaxLength = 30;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Amount"].MinValue = 0;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Amount"].MaxValue = new decimal(999999999999L);
			dataGridExpense.DisplayLayout.Bands[0].Columns["Amount"].CellAppearance.TextHAlign = HAlign.Right;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Amount"].Format = Format.GridAmountFormat;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Rate"].MinValue = 0;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Rate"].MaxValue = new decimal(999999999999L);
			dataGridExpense.DisplayLayout.Bands[0].Columns["Rate"].CellAppearance.TextHAlign = HAlign.Right;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Rate"].Format = Format.GridAmountFormat;
			dataGridExpense.DisplayLayout.Bands[0].Columns["FeeCode"].Width = 100;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Ref"].Width = 100;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Amount"].Width = 70;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Currency"].Width = 70;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Rate"].Width = 70;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Description"].Width = 250;
			dataGridExpense.DisplayLayout.Bands[0].Columns["TaxOption"].Hidden = true;
			dataGridExpense.DisplayLayout.Bands[0].Columns["TaxGroupID"].Hidden = true;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].Hidden = !CompanyPreferences.IsTax;
			Color color2 = dataGridExpense.DisplayLayout.Bands[0].Columns["TaxOption"].CellAppearance.BackColorDisabled = (dataGridExpense.DisplayLayout.Bands[0].Columns["TaxGroupID"].CellAppearance.BackColorDisabled = Color.WhiteSmoke);
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].CellAppearance.BackColor = Color.WhiteSmoke;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].CellAppearance.BackColorDisabled = Color.WhiteSmoke;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].TabStop = false;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].CellActivation = Activation.NoEdit;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].CellAppearance.TextHAlign = HAlign.Right;
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].Header.Appearance.ForeColor = Color.FromArgb(0, 0, 255);
			dataGridExpense.DisplayLayout.Bands[0].Columns["Tax"].Header.Appearance.Cursor = Cursors.Hand;
		}

		private void payeeSelector1_SelectedItemChanged(object sender, EventArgs e)
		{
			textBoxPayeeName.Text = payeeSelector1.SelectedName;
			if (payeeSelector1.SelectedType == "V")
			{
				buttonSelectInvoice.Enabled = true;
			}
			else
			{
				buttonSelectInvoice.Enabled = false;
			}
			if (payeeSelector1.SelectedType == "A")
			{
				comboBoxAnalysis.FilterByAccount(payeeSelector1.SelectedID);
				labelAnalysis.Visible = true;
				comboBoxAnalysis.Visible = true;
			}
			else
			{
				comboBoxAnalysis.Clear();
				comboBoxAnalysis.FilterByAccount("$#$$LDF");
				labelAnalysis.Visible = false;
				comboBoxAnalysis.Visible = false;
			}
			if (payeeSelector1.SelectedID != "")
			{
				if (payeeSelector1.SelectedType == "C" && ShowCustomerBal)
				{
					DataSet customerSnapBalance = Factory.CustomerSystem.GetCustomerSnapBalance(payeeSelector1.SelectedID);
					decimal d = decimal.Parse(customerSnapBalance.Tables[0].Rows[0]["Balance"].ToString());
					decimal d2 = decimal.Parse(customerSnapBalance.Tables[0].Rows[0]["PDCAmount"].ToString());
					textBoxBalance.Text = (d - d2).ToString(Format.TotalAmountFormat);
				}
				else if (payeeSelector1.SelectedType == "V" && ShowSupplierBal)
				{
					DataSet vendorBalanceAmount = Factory.VendorSystem.GetVendorBalanceAmount(payeeSelector1.SelectedID);
					decimal d3 = decimal.Parse(vendorBalanceAmount.Tables[0].Rows[0]["Balance"].ToString());
					decimal d4 = decimal.Parse(vendorBalanceAmount.Tables[0].Rows[0]["PDCAmount"].ToString());
					textBoxBalance.Text = (d3 - d4).ToString(Format.TotalAmountFormat);
					decimal num = default(decimal);
					vendorBalanceAmount = Factory.VendorSystem.GetVendorDueBalanceSummary(payeeSelector1.SelectedID, currencySelector.SelectedID, dateTimePickerDate.Value);
					if (vendorBalanceAmount.Tables[0].Rows.Count > 0)
					{
						num = decimal.Parse(vendorBalanceAmount.Tables[0].Rows[0]["BalanceDue"].ToString());
						textBoxTotalDue.Text = num.ToString(Format.TotalAmountFormat);
					}
					if (payeeSelector1.AllowOAP)
					{
						textBoxAmount.ReadOnly = false;
					}
					else
					{
						textBoxAmount.ReadOnly = true;
					}
				}
				else if (payeeSelector1.SelectedType == "E" && ShowEmployeeBal)
				{
					decimal num2 = decimal.Parse(Factory.EmployeeSystem.GetEmployeeSnapBalance(payeeSelector1.SelectedID).Tables[0].Rows[0]["Balance"].ToString());
					textBoxBalance.Text = num2.ToString(Format.TotalAmountFormat);
				}
				else if (payeeSelector1.SelectedType == "A" && ShowAccountBal)
				{
					decimal num3 = decimal.Parse(Factory.JournalSystem.GetAccountSnapBalance(payeeSelector1.SelectedID).Tables[0].Rows[0]["Balance"].ToString());
					textBoxBalance.Text = num3.ToString(Format.TotalAmountFormat);
				}
				else
				{
					textBoxBalance.Text = "";
				}
				if (payeeSelector1.SelectedType == "V")
				{
					bool result = false;
					bool.TryParse(Factory.DatabaseSystem.GetFieldValue("Vendor", "IsHoldForPayment", "VendorID", payeeSelector1.SelectedID).ToString(), out result);
					if (result && IsNewRecord)
					{
						ErrorHelper.WarningMessage("This vendor is on hold status and does not allow transaction.");
						return;
					}
				}
			}
			else
			{
				textBoxBalance.Text = "";
			}
			if (textBoxAmount.Tag != null)
			{
				textBoxAmount.Tag = null;
				textBoxAmount.Clear();
			}
		}

		private void comboBoxCostCenter_SelectedIndexChanged(object sender, EventArgs e)
		{
		}

		private void comboBoxSysDoc_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (isNewRecord)
			{
				textBoxVoucherNumber.Text = GetNextVoucherNumber();
			}
			formManager.SetControlDirtyStatus(textBoxVoucherNumber, textBoxVoucherNumber.Text);
		}

		private void SetRowLCAmount(UltraGridRow row)
		{
			decimal result = default(decimal);
			decimal.TryParse(row.Cells["Amount"].Value.ToString(), out result);
			decimal num = 1m;
			if (row.Cells["Rate"].Value.ToString() != "")
			{
				num = decimal.Parse(row.Cells["Rate"].Value.ToString());
			}
			string a = row.Cells["RateType"].Value.ToString();
			if (row.Cells["Currency"].Value.ToString() == "" || row.Cells["Currency"].Value.ToString() == Global.BaseCurrencyID)
			{
				num = 1m;
			}
			if (row.Cells["Currency"].Value.ToString() != "" && row.Cells["Currency"].Value.ToString() != Global.BaseCurrencyID && num > 0m)
			{
				if (a == "D")
				{
					result /= num;
				}
				else if (a == "M")
				{
					result *= num;
				}
			}
			row.Cells["AmountLC"].Value = result.ToString(Format.TotalAmountFormat);
			CalculateTotalExpense();
		}

		private void CalculateTotalExpense()
		{
			decimal d = default(decimal);
			decimal d2 = default(decimal);
			string taxGroupID = "";
			foreach (UltraGridRow row in dataGridExpense.Rows)
			{
				decimal result = default(decimal);
				if (row.Cells["AmountLC"].Value != null && !(row.Cells["AmountLC"].Value.ToString() == ""))
				{
					decimal.TryParse(row.Cells["AmountLC"].Value.ToString(), out result);
					d += result;
					if (!row.Cells["Tax"].Value.IsNullOrEmpty())
					{
						d2 += decimal.Parse(row.Cells["Tax"].Value.ToString());
					}
					if (!row.Cells["TaxGroupID"].Value.IsNullOrEmpty())
					{
						taxGroupID = row.Cells["TaxGroupID"].Value.ToString();
					}
				}
			}
			textBoxTotalExpense.Text = (d + d2).ToString(Format.TotalAmountFormat);
			textBoxTotalFees.Text = (d + d2).ToString();
			CalculateTotalTaxes(taxGroupID);
		}

		private void CalculateTotalTaxes(string taxGroupID)
		{
			TaxTransactionData taxTransactionData = TaxHelper.CreateTaxDetailData(PayeeTaxOptions.Taxable, taxGroupID);
			DataTable taxDetailTable = taxTransactionData.TaxDetailTable;
			foreach (UltraGridRow row in dataGridExpense.Rows)
			{
				if (row.Cells["Tax"].Tag != null)
				{
					foreach (DataRow row2 in (row.Cells["Tax"].Tag as TaxTransactionData).TaxDetailTable.Rows)
					{
						string text = row2["TaxItemID"].ToString();
						decimal result = default(decimal);
						decimal.TryParse(row2["TaxAmount"].ToString(), out result);
						DataRow[] array = taxDetailTable.Select("TaxItemID  = '" + text + "'");
						if (array.Count() > 0)
						{
							decimal result2 = default(decimal);
							decimal.TryParse(array[0]["TaxAmount"].ToString(), out result2);
							result2 += result;
							array[0]["TaxAmount"] = result2;
						}
						else
						{
							DataRow dataRow = taxDetailTable.NewRow();
							dataRow["TaxItemID"] = text;
							dataRow["TaxAmount"] = result;
							taxDetailTable.Rows.Add(dataRow);
						}
					}
				}
			}
			textBoxTaxAmount.Tag = taxTransactionData;
		}

		private bool GetData()
		{
			try
			{
				if (currentData == null || isNewRecord)
				{
					currentData = new TransactionData();
				}
				DataRow dataRow = (!isNewRecord) ? currentData.TransactionTable.Rows[0] : currentData.TransactionTable.NewRow();
				dataRow["TransactionID"] = 0;
				dataRow["SysDocType"] = (byte)64;
				if (textBoxNote.Text.Trim() != "")
				{
					dataRow["Description"] = textBoxNote.Text;
				}
				else
				{
					dataRow["Description"] = textBoxNote.Text;
				}
				if (textBoxRequest.Text != "")
				{
					dataRow["RequestSysDocID"] = requestSysDocID;
					dataRow["RequestVoucherID"] = textBoxRequest.Text;
				}
				else
				{
					dataRow["RequestSysDocID"] = DBNull.Value;
					dataRow["RequestVoucherID"] = DBNull.Value;
				}
				dataRow["CostCenterID"] = comboBoxCostCenter.SelectedID;
				dataRow["TransactionDate"] = dateTimePickerDate.Value;
				dataRow["SysDocID"] = comboBoxSysDoc.SelectedID;
				dataRow["VoucherID"] = textBoxVoucherNumber.Text;
				dataRow["Reference"] = textBoxRef1.Text;
				dataRow["CompanyID"] = Global.CompanyID;
				dataRow["DivisionID"] = comboBoxSysDoc.DivisionID;
				string text = (string)(dataRow["PayeeType"] = payeeSelector1.SelectedType);
				dataRow["PayeeID"] = payeeSelector1.SelectedID;
				if (currencySelector.SelectedID != "" && currencySelector.SelectedID != Global.BaseCurrencyID)
				{
					dataRow["CurrencyID"] = currencySelector.SelectedID;
					dataRow["CurrencyRate"] = currencySelector.Rate;
					dataRow["AmountFC"] = textBoxAmount.Text;
				}
				else
				{
					dataRow["CurrencyID"] = DBNull.Value;
					dataRow["CurrencyRate"] = 1;
					dataRow["Amount"] = textBoxAmount.Text;
				}
				dataRow.EndEdit();
				if (IsNewRecord)
				{
					currentData.TransactionTable.Rows.Add(dataRow);
				}
				currentData.TransactionDetailsTable.Rows.Clear();
				DataRow dataRow2 = currentData.TransactionDetailsTable.NewRow();
				dataRow2.BeginEdit();
				decimal num = Convert.ToDecimal(textBoxAmount.Text);
				dataRow2["AccountID"] = comboBoxBankAccount.SelectedID;
				dataRow2["Description"] = textBoxDescription.Text;
				dataRow2["PaymentMethodType"] = (byte)1;
				if (currencySelector.SelectedID == "" || currencySelector.IsBaseCurrency)
				{
					dataRow2["Amount"] = num;
					dataRow2["AmountFC"] = DBNull.Value;
				}
				else
				{
					dataRow2["AmountFC"] = num;
				}
				if (comboBoxJob.SelectedID != null && comboBoxJob.SelectedID.ToString() != "")
				{
					dataRow2["JobID"] = comboBoxJob.SelectedID;
				}
				else
				{
					dataRow2["JobID"] = DBNull.Value;
				}
				if (comboBoxCostCategory.SelectedID != null && comboBoxCostCategory.SelectedID.ToString() != "")
				{
					dataRow2["CostCategoryID"] = comboBoxCostCategory.SelectedID.ToString();
				}
				else
				{
					dataRow2["CostCategoryID"] = DBNull.Value;
				}
				if (comboBoxAnalysis.SelectedID != null && comboBoxAnalysis.SelectedID.ToString() != "")
				{
					dataRow2["AnalysisID"] = comboBoxAnalysis.SelectedID.ToString();
				}
				else
				{
					dataRow2["AnalysisID"] = DBNull.Value;
				}
				dataRow2["RowIndex"] = 0;
				dataRow2.EndEdit();
				currentData.TransactionDetailsTable.Rows.Add(dataRow2);
				currentData.BankFeeDetailsTable.Rows.Clear();
				decimal num2 = default(decimal);
				foreach (UltraGridRow row in dataGridExpense.Rows)
				{
					DataRow dataRow3 = currentData.BankFeeDetailsTable.NewRow();
					dataRow3.BeginEdit();
					dataRow3["GLTransactionSysDocID"] = comboBoxSysDoc.SelectedID;
					dataRow3["GLTransactionVoucherID"] = textBoxVoucherNumber.Text;
					dataRow3["BankFeeID"] = row.Cells["FeeCode"].Value.ToString();
					dataRow3["Description"] = row.Cells["Description"].Value.ToString();
					dataRow3["Reference"] = row.Cells["Ref"].Value.ToString();
					dataRow3["ExpenseAccountID"] = row.Cells["ExpenseAccountID"].Value.ToString();
					dataRow3["BankAccountID"] = comboBoxBankAccount.SelectedID;
					dataRow3["RowIndex"] = row.Index;
					if (!row.Cells["TaxOption"].Value.IsNullOrEmpty())
					{
						dataRow3["TaxOption"] = row.Cells["TaxOption"].Value.ToString();
					}
					else
					{
						dataRow3["TaxOption"] = (byte)2;
					}
					if (row.Cells["Tax"].Value != null && row.Cells["Tax"].Value.ToString() != "")
					{
						dataRow3["TaxAmount"] = row.Cells["Tax"].Value.ToString();
						num2 += decimal.Parse(row.Cells["Tax"].Value.ToString());
					}
					else
					{
						dataRow3["TaxAmount"] = DBNull.Value;
					}
					if (row.Cells["TaxGroupID"].Value != null && row.Cells["TaxGroupID"].Value.ToString() != "")
					{
						dataRow3["TaxGroupID"] = row.Cells["TaxGroupID"].Value.ToString();
					}
					else
					{
						dataRow3["TaxGroupID"] = DBNull.Value;
					}
					string a = row.Cells["Currency"].Value.ToString();
					if (a == "" || a == Global.BaseCurrencyID)
					{
						dataRow3["Amount"] = row.Cells["Amount"].Value.ToString();
					}
					else
					{
						dataRow3["AmountFC"] = row.Cells["Amount"].Value.ToString();
						dataRow3["Amount"] = row.Cells["AmountLC"].Value.ToString();
					}
					dataRow3["CurrencyID"] = row.Cells["Currency"].Value.ToString();
					dataRow3["CurrencyRate"] = row.Cells["Rate"].Value.ToString();
					dataRow3.EndEdit();
					currentData.BankFeeDetailsTable.Rows.Add(dataRow3);
				}
				if (num2 > 0m)
				{
					dataRow["TaxAmount"] = num2;
				}
				else
				{
					dataRow["TaxGroupID"] = DBNull.Value;
					dataRow["TaxAmount"] = 0;
				}
				if (textBoxAmount.Tag != null)
				{
					DataSet dataSet = textBoxAmount.Tag as DataSet;
					dataSet = dataSet.Copy();
					if (currentData.Tables.Contains("AP_Payment_Advice"))
					{
						currentData.Tables.Remove("AP_Payment_Advice");
					}
					string a2 = Global.BaseCurrencyID;
					foreach (DataRow row2 in dataSet.Tables["AP_Payment_Advice"].Rows)
					{
						if (!row2["CurrencyID"].IsDBNullOrEmpty())
						{
							a2 = row2["CurrencyID"].ToString();
						}
						row2["PaymentSysDocID"] = comboBoxSysDoc.SelectedID;
						row2["PaymentVoucherID"] = textBoxVoucherNumber.Text;
						row2["AllocationDate"] = dateTimePickerDate.Value;
					}
					if (a2 != currencySelector.SelectedID)
					{
						ErrorHelper.WarningMessage("Currency should not change after selecting invoices.");
						return false;
					}
					currentData.Merge(dataSet.Tables["AP_Payment_Advice"]);
				}
				currentData.Tables["Tax_Detail"].Rows.Clear();
				string selectedID = comboBoxSysDoc.SelectedID;
				string text2 = textBoxVoucherNumber.Text;
				int num3 = 0;
				foreach (UltraGridRow row3 in dataGridExpense.Rows)
				{
					if (row3.Cells["Tax"].Tag != null)
					{
						TaxHelper.CreateTaxRows(currentData, row3.Cells["Tax"].Tag as TaxTransactionData, TaxDetailLevel.Items, selectedID, text2, num3, currencySelector.SelectedID, currencySelector.Rate);
					}
					num3 = checked(num3 + 1);
				}
				if (textBoxTaxAmount.Tag != null)
				{
					TaxHelper.CreateTaxRows(currentData, textBoxTaxAmount.Tag as TaxTransactionData, TaxDetailLevel.Transaction, selectedID, text2, -1, Global.DefaultCurrencySign, 1m);
				}
				return true;
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void buttonSave_Click(object sender, EventArgs e)
		{
			SaveData();
		}

		public void LoadData(string journalID)
		{
			try
			{
				if (!(journalID.Trim() == "") && CanClose())
				{
					currentData = Factory.TransactionSystem.GetTransactionByID(SystemDocID, journalID);
					if (currentData != null)
					{
						FillData();
						IsNewRecord = false;
						formManager.ResetDirty();
					}
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				ClearForm();
			}
		}

		private void FillData()
		{
			try
			{
				if (currentData != null && currentData.Tables.Count != 0 && currentData.Tables[0].Rows.Count != 0)
				{
					DataRow dataRow = currentData.Tables["GL_Transaction"].Rows[0];
					dateTimePickerDate.Value = DateTime.Parse(dataRow["TransactionDate"].ToString());
					textBoxVoucherNumber.Text = dataRow["VoucherID"].ToString();
					textBoxRef1.Text = dataRow["Reference"].ToString();
					comboBoxCostCenter.SelectedID = dataRow["CostCenterID"].ToString();
					textBoxNote.Text = dataRow["Description"].ToString();
					payeeSelector1.SelectedType = dataRow["PayeeType"].ToString();
					payeeSelector1.SelectedID = dataRow["PayeeID"].ToString();
					comboBoxAnalysis.SelectedID = dataRow["AnalysisID"].ToString();
					requestSysDocID = dataRow["RequestSysDocID"].ToString();
					textBoxRequest.Text = dataRow["RequestVoucherID"].ToString();
					if (textBoxRequest.Text != "")
					{
						payeeSelector1.Enabled = false;
						comboBoxBankAccount.Enabled = false;
					}
					if (dataRow["CurrencyID"] != DBNull.Value)
					{
						currencySelector.SelectedID = dataRow["CurrencyID"].ToString();
						currencySelector.Rate = decimal.Parse(dataRow["CurrencyRate"].ToString());
					}
					else
					{
						currencySelector.SelectedID = "";
						currencySelector.Rate = 1m;
					}
					if (dataRow["IsVoid"] != DBNull.Value)
					{
						IsVoid = bool.Parse(dataRow["IsVoid"].ToString());
					}
					else
					{
						IsVoid = false;
					}
					if (currentData.Tables.Contains("Transaction_Details") && currentData.TransactionDetailsTable.Rows.Count != 0)
					{
						DataRow dataRow2 = currentData.Tables["Transaction_Details"].Rows[0];
						if (dataRow2["AmountFC"] != DBNull.Value)
						{
							textBoxAmount.Text = Math.Round(decimal.Parse(dataRow2["AmountFC"].ToString()), Global.CurDecimalPoints).ToString(Format.TotalAmountFormat);
						}
						else if (dataRow2["Amount"] != DBNull.Value)
						{
							textBoxAmount.Text = Math.Round(decimal.Parse(dataRow2["Amount"].ToString()), Global.CurDecimalPoints).ToString(Format.TotalAmountFormat);
						}
						else
						{
							textBoxAmount.Text = 0.ToString(Format.TotalAmountFormat);
						}
						comboBoxBankAccount.SelectedID = dataRow2["AccountID"].ToString();
						textBoxDescription.Text = dataRow2["Description"].ToString();
						if (dataRow2["JobID"] != DBNull.Value)
						{
							comboBoxJob.SelectedID = dataRow2["JobID"].ToString();
						}
						else
						{
							comboBoxJob.Clear();
						}
						if (dataRow2["CostCategoryID"] != DBNull.Value)
						{
							comboBoxCostCategory.SelectedID = dataRow2["CostCategoryID"].ToString();
						}
						else
						{
							comboBoxCostCategory.Clear();
						}
						if (dataRow2["AnalysisID"] != DBNull.Value)
						{
							comboBoxAnalysis.SelectedID = dataRow2["AnalysisID"].ToString();
						}
						else
						{
							comboBoxAnalysis.Clear();
						}
						DataTable dataTable = dataGridExpense.DataSource as DataTable;
						dataTable.Clear();
						textBoxTotalExpense.Text = 0.ToString(Format.TotalAmountFormat);
						foreach (DataRow row in currentData.Tables["Bank_Fee_Details"].Rows)
						{
							DataRow dataRow4 = dataTable.NewRow();
							bool flag = false;
							dataRow4["FeeCode"] = row["BankFeeID"];
							dataRow4["Description"] = row["Description"];
							dataRow4["Currency"] = row["CurrencyID"];
							dataRow4["Ref"] = row["Reference"];
							dataRow4["Rate"] = row["CurrencyRate"];
							dataRow4["RateType"] = row["RateType"];
							dataRow4["ExpenseAccountID"] = row["ExpenseAccountID"];
							if (row["TaxOption"] != DBNull.Value)
							{
								dataRow4["TaxOption"] = byte.Parse(row["TaxOption"].ToString());
							}
							else
							{
								dataRow4["TaxOption"] = ItemTaxOptions.NonTaxable;
							}
							if (row["TaxAmount"] != DBNull.Value)
							{
								dataRow4["Tax"] = decimal.Parse(row["TaxAmount"].ToString()).ToString(Format.UnitPriceFormat);
							}
							if (!row["TaxGroupID"].IsDBNullOrEmpty())
							{
								dataRow4["TaxGroupID"] = row["TaxGroupID"];
							}
							if (row["CurrencyID"].ToString() != "" && row["CurrencyID"].ToString() != Global.BaseCurrencyID)
							{
								flag = true;
							}
							dataRow4["Rate"] = row["CurrencyRate"];
							if (flag)
							{
								dataRow4["Amount"] = decimal.Parse(row["AmountFC"].ToString()).ToString(Format.TotalAmountFormat);
							}
							else
							{
								dataRow4["Amount"] = decimal.Parse(row["Amount"].ToString()).ToString(Format.TotalAmountFormat);
							}
							dataRow4.EndEdit();
							dataTable.Rows.Add(dataRow4);
						}
						dataTable.AcceptChanges();
						foreach (UltraGridRow row2 in dataGridExpense.Rows)
						{
							SetRowLCAmount(row2);
						}
						foreach (UltraGridRow row3 in dataGridExpense.Rows)
						{
							DataRow[] array = currentData.TaxDetailsTable.Select("RowIndex = " + row3.Index + " AND TaxLevel = " + (byte)2);
							if (array.Length != 0)
							{
								TaxTransactionData taxTransactionData = new TaxTransactionData();
								taxTransactionData.Merge(array);
								row3.Cells["Tax"].Tag = taxTransactionData;
							}
						}
						if (currentData.Tables["AP_Payment_Advice"].Rows.Count > 0)
						{
							textBoxAmount.Tag = currentData;
							textBoxAmount.ReadOnly = true;
						}
						DataRow[] array2 = currentData.TaxDetailsTable.Select("RowIndex = -1 AND TaxLevel = " + (byte)1);
						if (array2.Length != 0)
						{
							new TaxTransactionData().Merge(array2);
						}
						CalculateTotalExpense();
					}
				}
			}
			catch
			{
				throw;
			}
		}

		private bool SaveData()
		{
			if (!IsDirty)
			{
				if (!IsNewRecord)
				{
					IsNewRecord = true;
					ClearForm();
				}
				return true;
			}
			if (!IsNewRecord)
			{
				switch (ErrorHelper.QuestionMessageYesNoCancel(UIMessages.DoYouWantToSave))
				{
				case DialogResult.No:
					return true;
				case DialogResult.Cancel:
					return false;
				}
			}
			return SaveData(clearAfter: true);
		}

		private bool SaveData(bool clearAfter)
		{
			if (!ValidateData())
			{
				return false;
			}
			if (!GetData())
			{
				return false;
			}
			bool flag = false;
			try
			{
				bool flag2 = (!isNewRecord) ? Factory.TransactionSystem.UpdateTransaction(currentData) : Factory.TransactionSystem.CreateTransaction(currentData);
				if (flag2)
				{
					flag = true;
				}
				if (!flag2)
				{
					ErrorHelper.ErrorMessage();
				}
				else
				{
					if (showAllocationForm && textBoxAmount.Tag == null && payeeSelector1.SelectedType == "V")
					{
						CustomerPaymentAllocationForm customerPaymentAllocationForm = new CustomerPaymentAllocationForm();
						customerPaymentAllocationForm.IsARPayment = false;
						customerPaymentAllocationForm.SetData(comboBoxSysDoc.SelectedID, textBoxVoucherNumber.Text, payeeSelector1.SelectedID, -1, isPDC: false);
						customerPaymentAllocationForm.ShowDialog();
					}
					bool result = false;
					bool result2 = false;
					bool.TryParse(comboBoxSysDoc.GetSelectedCellValue("DoPrint").ToString(), out result);
					if (result)
					{
						bool.TryParse(comboBoxSysDoc.GetSelectedCellValue("PrintAfterSave").ToString(), out result2);
						if (result2)
						{
							Print(isPrint: true, showPrintDialog: true, saveChanges: false);
						}
						else
						{
							Print(isPrint: false, showPrintDialog: true, saveChanges: false);
						}
					}
					if (clearAfter)
					{
						ClearForm();
						IsNewRecord = true;
					}
					else
					{
						formManager.ResetDirty();
					}
				}
				return flag2;
			}
			catch (CompanyException ex)
			{
				if (ex.Number == 1046)
				{
					string nextVoucherNumber = GetNextVoucherNumber();
					if (nextVoucherNumber == textBoxVoucherNumber.Text)
					{
						ErrorHelper.WarningMessage(UIMessages.DocumentNumberInUse);
						return false;
					}
					if (nextVoucherNumber != "")
					{
						textBoxVoucherNumber.Text = nextVoucherNumber;
					}
					formManager.SetControlDirtyStatus(textBoxVoucherNumber, textBoxVoucherNumber.Text);
					return SaveData();
				}
				ErrorHelper.ProcessError(ex);
				return false;
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
			finally
			{
				if (flag)
				{
					if (clearAfter)
					{
						ClearForm();
						IsNewRecord = true;
					}
					else
					{
						formManager.ResetDirty();
					}
				}
			}
		}

		public void SetApprovalStatus()
		{
			if (IsNewRecord)
			{
				ToolStripButton toolStripButton = toolStripButtonApproval;
				ToolStripLabel toolStripLabel = toolStripLabelApproval;
				bool flag2 = toolStripSeparatorApproval.Visible = false;
				bool visible = toolStripLabel.Visible = flag2;
				toolStripButton.Visible = visible;
			}
			else
			{
				if (currentData == null || currentData.Tables[0].Rows.Count <= 0)
				{
					return;
				}
				DataRow dataRow = currentData.Tables[0].Rows[0];
				bool flag2;
				bool visible;
				if (!dataRow.Table.Columns.Contains("ApprovalStatus") || dataRow["ApprovalStatus"].IsDBNullOrEmpty())
				{
					ToolStripButton toolStripButton2 = toolStripButtonApproval;
					ToolStripLabel toolStripLabel2 = toolStripLabelApproval;
					flag2 = (toolStripSeparatorApproval.Visible = false);
					visible = (toolStripLabel2.Visible = flag2);
					toolStripButton2.Visible = visible;
					return;
				}
				switch (int.Parse(dataRow["ApprovalStatus"].ToString()))
				{
				case 3:
					toolStripButtonApproval.Text = "Rejected";
					toolStripButtonApproval.ForeColor = Color.Red;
					break;
				case 10:
					toolStripButtonApproval.Text = "Approved";
					toolStripButtonApproval.ForeColor = Color.ForestGreen;
					break;
				default:
					toolStripButtonApproval.Text = "Pending";
					toolStripButtonApproval.ForeColor = Color.Orange;
					break;
				}
				ToolStripButton toolStripButton3 = toolStripButtonApproval;
				ToolStripLabel toolStripLabel3 = toolStripLabelApproval;
				flag2 = (toolStripSeparatorApproval.Visible = true);
				visible = (toolStripLabel3.Visible = flag2);
				toolStripButton3.Visible = visible;
			}
		}

		public void ShowForApproval(string sysDocID, string voucherID, int approvalTaskID)
		{
			EditDocument(sysDocID, voucherID);
			panelButtons.Visible = false;
			toolStrip1.Enabled = false;
			formManager.ShowApprovalPanel(approvalTaskID, "GL_Transaction", "VoucherID");
		}

		private bool ValidateData()
		{
			if (!screenRight.New && isNewRecord)
			{
				ErrorHelper.WarningMessage(UIMessages.NoPermissionNew);
				return false;
			}
			if (!screenRight.Edit && !isNewRecord)
			{
				ErrorHelper.WarningMessage(UIMessages.NoPermissionEdit);
				return false;
			}
			if (!IsNewRecord && !Global.IsUserAdmin && !AllowEditTransaction && Global.CurrentUser != Factory.SystemDocumentSystem.GetTransUserID("GL_Transaction", "VoucherID", SystemDocID, textBoxVoucherNumber.Text))
			{
				ErrorHelper.WarningMessage("You dont have permission to edit.");
				return false;
			}
			if (!Factory.SystemDocumentSystem.HasuserAccess(comboBoxSysDoc.SelectedID, Global.DefaultLocationID) && !Global.IsUserAdmin && !AllowEditTransDiffLocation)
			{
				ErrorHelper.WarningMessage("You dont have permission to edit (SecurityRoleID:117).");
				return false;
			}
			DateTime t = new DateTime(DateTime.Now.Year, DateTime.Now.Month, DateTime.Now.Day, 23, 59, 59);
			if (isNewRecord && dateTimePickerDate.Value < t && !Security.IsAllowedSecurityRole(GeneralSecurityRoles.EnterBackDatedTransaction))
			{
				ErrorHelper.WarningMessage("You are not allowed to enter back-dated transactions.");
				return false;
			}
			if (isNewRecord && dateTimePickerDate.Value > t && !Security.IsAllowedSecurityRole(GeneralSecurityRoles.FutureDatedTransaction))
			{
				ErrorHelper.WarningMessage("You are not allowed to enter future-dated transactions.");
				return false;
			}
			if (comboBoxBankAccount.SelectedID == "" || comboBoxSysDoc.SelectedID == "" || textBoxVoucherNumber.Text.Trim() == "" || payeeSelector1.SelectedID == "")
			{
				ErrorHelper.InformationMessage(UIMessages.EnterRequiredFields);
				return false;
			}
			if (isCostCenterMandatory && comboBoxCostCenter.SelectedID == string.Empty)
			{
				ErrorHelper.InformationMessage("Please select cost center");
				return false;
			}
			if (formManager.IsFieldDirty(textBoxVoucherNumber) && Factory.SystemDocumentSystem.ExistDocumentNumber("GL_Transaction", "VoucherID", SystemDocID, textBoxVoucherNumber.Text))
			{
				ErrorHelper.WarningMessage(UIMessages.DocumentNumberInUse);
				textBoxVoucherNumber.Focus();
				return false;
			}
			if (payeeSelector1.SelectedType == "V" && payeeSelector1.SelectedID != "")
			{
				bool result = false;
				bool.TryParse(Factory.DatabaseSystem.GetFieldValue("Vendor", "IsHoldForPayment", "VendorID", payeeSelector1.SelectedID).ToString(), out result);
				if (result && IsNewRecord)
				{
					ErrorHelper.WarningMessage("This vendor is on hold status and does not allow transaction.");
					return false;
				}
			}
			if (!IsNewRecord)
			{
				DataSet entityApprovalStatus = Factory.EntityDocSystem.GetEntityApprovalStatus(currentData, SysDocTypes.TTPayment, Global.CurrentUser, includeApproveUser: false);
				if (entityApprovalStatus.Tables[0].Rows.Count > 0 && !bool.Parse(entityApprovalStatus.Tables[0].Rows[0]["ModifyTransaction"].ToString()))
				{
					ErrorHelper.WarningMessage(UIMessages.NoPermissionEdit);
					return false;
				}
			}
			return true;
		}

		private decimal GetTransactionBalance()
		{
			return 0m;
		}

		private void buttonNew_Click(object sender, EventArgs e)
		{
			if (IsNewRecord)
			{
				ClearForm();
			}
			else if (SaveData())
			{
				ClearForm();
				IsNewRecord = true;
			}
		}

		private void ClearForm()
		{
			try
			{
				textBoxNote.Clear();
				comboBoxBankAccount.Clear();
				textBoxRef1.Clear();
				dateTimePickerDate.Value = DateTime.Now;
				buttonSelectInvoice.Enabled = true;
				textBoxAmount.ReadOnly = false;
				textBoxAmount.Tag = null;
				textBoxVoucherNumber.Text = GetNextVoucherNumber();
				comboBoxAnalysis.Clear();
				payeeSelector1.Clear();
				textBoxPayeeName.Clear();
				textBoxDescription.Clear();
				textBoxAmount.Text = 0.ToString(Format.TotalAmountFormat);
				comboBoxJob.Clear();
				comboBoxCostCategory.Clear();
				if (payeeSelector1.SelectedType == "")
				{
					payeeSelector1.SelectedType = "V";
				}
				comboBoxSysDoc.SetDefaultID(Security.DefaultTransactionLocationID);
				textBoxRequest.Clear();
				requestSysDocID = "";
				payeeSelector1.Enabled = true;
				comboBoxBankAccount.Enabled = true;
				textBoxTotalFees.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxBalance.Text = 0.ToString(Format.TotalAmountFormat);
				textBoxRegBalance.Text = 0.ToString(Format.TotalAmountFormat);
				(dataGridExpense.DataSource as DataTable).Rows.Clear();
				SetApprovalStatus();
				IsVoid = false;
				formManager.ResetDirty();
				dateTimePickerDate.Focus();
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		private void TransactionLeaveGroupDetailsForm_Validating(object sender, CancelEventArgs e)
		{
		}

		private void TransactionLeaveGroupDetailsForm_Validated(object sender, EventArgs e)
		{
		}

		private void buttonDelete_Click(object sender, EventArgs e)
		{
			if (Delete())
			{
				ClearForm();
				IsNewRecord = true;
			}
		}

		private bool Delete()
		{
			try
			{
				if (ErrorHelper.QuestionMessageYesNo(UIMessages.DeleteRecord) == DialogResult.No)
				{
					return false;
				}
				return Factory.TransactionSystem.DeleteTransaction(SystemDocID, textBoxVoucherNumber.Text);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void xpButton1_Click(object sender, EventArgs e)
		{
			Close();
		}

		private void toolStripButtonNext_Click(object sender, EventArgs e)
		{
			string nextID = DatabaseHelper.GetNextID("GL_Transaction", "VoucherID", textBoxVoucherNumber.Text, "SysDocID", SystemDocID);
			if (!(nextID == ""))
			{
				LoadData(nextID);
			}
		}

		private void toolStripButtonPrevious_Click(object sender, EventArgs e)
		{
			string previousID = DatabaseHelper.GetPreviousID("GL_Transaction", "VoucherID", textBoxVoucherNumber.Text, "SysDocID", SystemDocID);
			if (!(previousID == ""))
			{
				LoadData(previousID);
			}
		}

		private void toolStripButtonLast_Click(object sender, EventArgs e)
		{
			string lastID = DatabaseHelper.GetLastID("GL_Transaction", "VoucherID", "SysDocID", SystemDocID);
			if (!(lastID == ""))
			{
				LoadData(lastID);
			}
		}

		private void toolStripButtonFirst_Click(object sender, EventArgs e)
		{
			string firstID = DatabaseHelper.GetFirstID("GL_Transaction", "VoucherID", "SysDocID", SystemDocID);
			if (!(firstID == ""))
			{
				LoadData(firstID);
			}
		}

		private void toolStripButtonFind_Click(object sender, EventArgs e)
		{
			try
			{
				if (toolStripTextBoxFind.Text.Trim() == "")
				{
					toolStripTextBoxFind.Focus();
				}
				else
				{
					string text = Factory.DatabaseSystem.FindDocumentByNumber("GL_Transaction", "VoucherID", SystemDocID, toolStripTextBoxFind.Text);
					if (text != "")
					{
						LoadData(text);
					}
					else
					{
						ErrorHelper.InformationMessage(UIMessages.DocumentNotFound);
						toolStripTextBoxFind.SelectAll();
						toolStripTextBoxFind.Focus();
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		public void OnActivated()
		{
		}

		private void AccountGroupDetailsForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			if (!CanClose())
			{
				e.Cancel = true;
			}
		}

		private bool CanClose()
		{
			if (IsDirty)
			{
				BringToFront();
				if (IsNewRecord)
				{
					switch (ErrorHelper.QuestionMessageYesNoCancel(UIMessages.DoYouWantToSave))
					{
					case DialogResult.Yes:
						if (!SaveData())
						{
							return false;
						}
						break;
					default:
						return false;
					case DialogResult.No:
						break;
					}
				}
				else if (!SaveData())
				{
					return false;
				}
			}
			return true;
		}

		private void TransactionLeavesForm_Load(object sender, EventArgs e)
		{
			try
			{
				UltraFormattedLinkLabel ultraFormattedLinkLabel = labelCurrency;
				bool visible = currencySelector.Visible = CompanyPreferences.UseMultiCurrency;
				ultraFormattedLinkLabel.Visible = visible;
				labelAmountBase.Text = "Amount (" + Global.BaseCurrencyID + "):";
				SetupExpenseGrid();
				SetSecurity();
				if (!base.IsDisposed)
				{
					dateTimePickerDate.Value = DateTime.Now;
					IsNewRecord = true;
					ClearForm();
					comboBoxSysDoc.FilterByType(SysDocTypes.TTPayment);
				}
			}
			catch (Exception e2)
			{
				dataGridExpense.LoadLayoutFailed = true;
				ErrorHelper.ProcessError(e2);
			}
		}

		private void SetSecurity()
		{
			screenRight = Security.GetScreenAccessRight(base.Name);
			if (!screenRight.View)
			{
				ErrorHelper.ErrorMessage(UIMessages.NoPermissionView);
				Close();
				return;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.ChangeDocNumber))
			{
				textBoxVoucherNumber.ReadOnly = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessSupplierBal))
			{
				ShowSupplierBal = false;
			}
			else
			{
				ShowSupplierBal = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessCustomerBal))
			{
				ShowCustomerBal = false;
			}
			else
			{
				ShowCustomerBal = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessAccountBal))
			{
				ShowAccountBal = false;
			}
			else
			{
				ShowAccountBal = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.AccessEmployeeBal))
			{
				ShowEmployeeBal = false;
			}
			else
			{
				ShowEmployeeBal = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.EditTransaction))
			{
				AllowEditTransaction = false;
			}
			else
			{
				AllowEditTransaction = true;
			}
			if (!Security.IsAllowedSecurityRole(GeneralSecurityRoles.EditTransDiffLocation))
			{
				AllowEditTransDiffLocation = false;
			}
			else
			{
				AllowEditTransDiffLocation = true;
			}
		}

		private void ultraFormattedLinkLabel1_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditCurrency(currencySelector.SelectedID);
		}

		private void ultraFormattedLinkLabel2_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			textBoxVoucherNumber.Text = GetNextVoucherNumber();
		}

		private string GetNextVoucherNumber()
		{
			try
			{
				return Factory.SystemDocumentSystem.GetNextDocumentNumber(SystemDocID);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return "";
			}
		}

		private void buttonVoid_Click(object sender, EventArgs e)
		{
			if (Void(!IsVoid))
			{
				IsVoid = !IsVoid;
			}
		}

		private bool Void(bool isVoid)
		{
			try
			{
				DialogResult dialogResult = (!isVoid) ? ErrorHelper.QuestionMessageYesNo(UIMessages.WantToUnvoid) : ErrorHelper.QuestionMessageYesNo(UIMessages.WantToVoid);
				if (dialogResult == DialogResult.No)
				{
					return false;
				}
				return Factory.TransactionSystem.VoidTransaction(SystemDocID, textBoxVoucherNumber.Text, isVoid);
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void ultraFormattedLinkLabel3_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			string selectedType = payeeSelector1.SelectedType;
			if (!(selectedType == ""))
			{
				FormHelper formHelper = new FormHelper();
				if (selectedType == "A")
				{
					formHelper.EditAccount(payeeSelector1.SelectedID);
				}
				else if (selectedType == "C")
				{
					formHelper.EditCustomer(payeeSelector1.SelectedID);
				}
				else if (selectedType == "V")
				{
					formHelper.EditVendor(payeeSelector1.SelectedID);
				}
				else if (selectedType == "E")
				{
					formHelper.EditEmployee(payeeSelector1.SelectedID);
				}
			}
		}

		private void ultraFormattedLinkLabel4_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditCostCenter(comboBoxCostCenter.SelectedID);
		}

		private void ultraFormattedLinkLabel5_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditSysDoc(comboBoxSysDoc.SelectedID, SysDocTypes.TTPayment);
		}

		private void ultraFormattedLinkLabel6_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditAccount(comboBoxBankAccount.SelectedID);
		}

		private void toolStripButtonPrint_Click(object sender, EventArgs e)
		{
			Print(isPrint: true, showPrintDialog: true, saveChanges: true);
		}

		private void Print()
		{
			Print(isPrint: true, showPrintDialog: false, saveChanges: true);
		}

		private void Print(bool isPrint, bool showPrintDialog, bool saveChanges)
		{
			try
			{
				if (!(IsDirty && saveChanges) || (ErrorHelper.QuestionMessage(MessageBoxButtons.YesNo, "You must save the document before printing.", "Do you want to save?") == DialogResult.Yes && SaveData(clearAfter: false)))
				{
					string systemDocID = SystemDocID;
					string text = textBoxVoucherNumber.Text;
					DataSet transactionToPrint = Factory.TransactionSystem.GetTransactionToPrint(systemDocID, text);
					if (transactionToPrint == null || transactionToPrint.Tables.Count == 0)
					{
						ErrorHelper.ErrorMessage("Cannot print the document.", "Document not found.");
					}
					else
					{
						PrintHelper.PrintDocument(transactionToPrint, systemDocID, "TT Payment", SysDocTypes.TTPayment, isPrint, showPrintDialog);
					}
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		private void toolStripButtonPreview_Click(object sender, EventArgs e)
		{
			Print(isPrint: false, showPrintDialog: false, saveChanges: true);
		}

		public void EditDocument(string sysDocID, string voucherID)
		{
			if (!comboBoxSysDoc.Enabled && sysDocID != comboBoxSysDoc.SelectedID)
			{
				ErrorHelper.ErrorMessage("Cannot edit this document because you do not have access to this document.");
				return;
			}
			comboBoxSysDoc.SelectedID = sysDocID;
			LoadData(voucherID);
		}

		private void labelVoided_Click(object sender, EventArgs e)
		{
		}

		private void toolStripButtonOpenList_Click(object sender, EventArgs e)
		{
			TransactionListForm paymentVoucherListObj = FormActivator.PaymentVoucherListObj;
			paymentVoucherListObj.PaymentType = TransactionPaymentType.TT;
			FormActivator.BringFormToFront(paymentVoucherListObj);
		}

		private void saveAsDraftToolStripMenuItem_Click(object sender, EventArgs e)
		{
			SaveDraft();
		}

		private bool SaveDraft()
		{
			try
			{
				if (GetData())
				{
					EnterNameDialog enterNameDialog = new EnterNameDialog();
					if (enterNameDialog.ShowDialog() == DialogResult.OK)
					{
						return Global.CompanySettings.SaveTransactionDraft(currentData, enterNameDialog.EnteredName, SysDocTypes.TTPayment);
					}
				}
				return false;
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private bool LoadDraft()
		{
			try
			{
				DataSet settingsList = Factory.SettingSystem.GetSettingsList("", 64.ToString());
				SelectDocumentDialog selectDocumentDialog = new SelectDocumentDialog();
				selectDocumentDialog.DataSource = settingsList;
				selectDocumentDialog.Text = "Select Draft";
				selectDocumentDialog.IsMultiSelect = false;
				if (selectDocumentDialog.ShowDialog(this) == DialogResult.OK)
				{
					string key = selectDocumentDialog.SelectedRow.Cells["Name"].Value.ToString();
					DataSet dataSet = Global.CompanySettings.LoadTransactionDraft(key, SysDocTypes.TTPayment);
					currentData = (dataSet as TransactionData);
					FillData();
				}
				return true;
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
				return false;
			}
		}

		private void loadDraftToolStripMenuItem_Click(object sender, EventArgs e)
		{
			if (CanClose())
			{
				LoadDraft();
			}
		}

		private void toolStripButtonAttach_Click(object sender, EventArgs e)
		{
			try
			{
				if (!isNewRecord)
				{
					DocManagementForm docManagementForm = new DocManagementForm();
					if (!(comboBoxSysDoc.SelectedID == "") || !(textBoxVoucherNumber.Text.Trim() == ""))
					{
						docManagementForm.EntityID = textBoxVoucherNumber.Text.Trim();
						docManagementForm.EntitySysDocID = comboBoxSysDoc.SelectedID;
						docManagementForm.EntityName = comboBoxSysDoc.SelectedID;
						docManagementForm.EntityType = EntityTypesEnum.Transactions;
						docManagementForm.ShowDialog(this);
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void ultraFormattedLinkLabel8_LinkClicked(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			DataSet dataSet = null;
			if (textBoxAmount.Tag != null)
			{
				dataSet = (textBoxAmount.Tag as DataSet);
				PaymentAdviceDetailsForm paymentAdviceDetailsForm = new PaymentAdviceDetailsForm();
				paymentAdviceDetailsForm.SetData(payeeSelector1.SelectedID, payeeSelector1.SelectedName, currencySelector.SelectedID, currencySelector.Rate);
				paymentAdviceDetailsForm.PaymentData = dataSet;
				paymentAdviceDetailsForm.IsViewOnly = true;
				paymentAdviceDetailsForm.ShowDialog();
			}
		}

		private void toolStripButtonDistribution_Click(object sender, EventArgs e)
		{
			JournalDistibutionDialog journalDistibutionDialog = new JournalDistibutionDialog();
			journalDistibutionDialog.VoucherID = textBoxVoucherNumber.Text;
			journalDistibutionDialog.SysDocID = comboBoxSysDoc.SelectedID;
			journalDistibutionDialog.ShowDialog(this);
		}

		private void buttonSelectInvoice_Click(object sender, EventArgs e)
		{
			string vendorID = "";
			if (payeeSelector1.SelectedType == "V")
			{
				vendorID = payeeSelector1.SelectedID;
			}
			SelectInvoicesToPay(vendorID, payeeSelector1.SelectedName, currencySelector.SelectedID);
		}

		private void dataGridExpense_AfterRowsDeleted(object sender, EventArgs e)
		{
			CalculateTotalExpense();
		}

		private void toolStripTextBoxFind_KeyPress(object sender, KeyPressEventArgs e)
		{
			if (e.KeyChar == Convert.ToChar(Keys.Return))
			{
				toolStripButtonFind_Click(sender, e);
			}
		}

		private void buttonSelectRequest_Click(object sender, EventArgs e)
		{
			try
			{
				DataSet openPaymentRequests = Factory.PaymentRequestSystem.GetOpenPaymentRequests(2);
				SelectDocumentDialog selectDocumentDialog = new SelectDocumentDialog();
				selectDocumentDialog.DataSource = openPaymentRequests;
				selectDocumentDialog.IsMultiSelect = false;
				selectDocumentDialog.Text = "Select Payment Request";
				if (selectDocumentDialog.ShowDialog(this) == DialogResult.OK)
				{
					UltraGridRow activeRow = selectDocumentDialog.Grid.ActiveRow;
					string sysDocID = activeRow.Cells["DocID"].Value.ToString();
					string text = activeRow.Cells["Number"].Value.ToString();
					PaymentRequestData paymentRequestByID = Factory.PaymentRequestSystem.GetPaymentRequestByID(sysDocID, text);
					if (paymentRequestByID != null && paymentRequestByID.Tables[0].Rows.Count > 0)
					{
						DataRow dataRow = paymentRequestByID.Tables[0].Rows[0];
						textBoxRequest.Text = text;
						requestSysDocID = sysDocID;
						payeeSelector1.SelectedID = dataRow["PayeeID"].ToString();
						payeeSelector1.SelectedType = "V";
						comboBoxBankAccount.SelectedID = dataRow["PayFromID"].ToString();
						if (!dataRow["AmountFC"].IsDBNullOrEmpty())
						{
							textBoxAmount.Text = dataRow["AmountFC"].ToString();
						}
						else
						{
							textBoxAmount.Text = dataRow["Amount"].ToString();
						}
						currencySelector.SelectedID = dataRow["CurrencyID"].ToString();
						payeeSelector1.Enabled = false;
						comboBoxBankAccount.Enabled = false;
					}
				}
			}
			catch (Exception e2)
			{
				ErrorHelper.ProcessError(e2);
			}
		}

		private void ultraFormattedLinkLabel1_LinkClicked_1(object sender, Infragistics.Win.FormattedLinkLabel.LinkClickedEventArgs e)
		{
			new FormHelper().EditTransaction(TransactionListType.PaymentRequest, requestSysDocID, textBoxRequest.Text);
		}

		private void toolStripButtonInformation_Click(object sender, EventArgs e)
		{
			if (!isNewRecord)
			{
				FormHelper.ShowDocumentInfo(textBoxVoucherNumber.Text, comboBoxSysDoc.SelectedID, this);
			}
		}

		private void SelectInvoicesToPay(string vendorID, string vendorName, string currencyID)
		{
			try
			{
				if (vendorID != "")
				{
					PaymentAdviceDetailsForm paymentAdviceDetailsForm = new PaymentAdviceDetailsForm();
					paymentAdviceDetailsForm.IsARPayment = false;
					paymentAdviceDetailsForm.SetData(vendorID, vendorName, currencyID, currencySelector.Rate);
					if (paymentAdviceDetailsForm.ShowDialog() == DialogResult.OK)
					{
						DataSet dataSet = new DataSet();
						DataTable dataTable = dataSet.Tables.Add("Invoice");
						dataTable.Columns.AddRange(new DataColumn[2]
						{
							new DataColumn("SysDocID"),
							new DataColumn("VoucherID")
						});
						foreach (DataRow row in paymentAdviceDetailsForm.PaymentData.Tables["AP_Payment_Advice"].Rows)
						{
							dataTable.Rows.Add(row["InvoiceSysDocID"].ToString(), row["InvoiceVoucherID"].ToString());
						}
						string text = Factory.PurchasePrepaymentInvoiceSystem.HasPendingPrepayments(dataSet);
						if (!(text != "") || ErrorHelper.WarningMessageYesNo("Invoice number '" + text + "' has unallocated prepayments.", "Are you sure you want to continue?") != DialogResult.No)
						{
							textBoxAmount.Tag = paymentAdviceDetailsForm.PaymentData;
							decimal d = default(decimal);
							foreach (DataRow row2 in paymentAdviceDetailsForm.PaymentData.Tables["AP_Payment_Advice"].Rows)
							{
								d += decimal.Parse(row2["PaymentAmount"].ToString());
							}
							textBoxAmount.Text = d.ToString(Format.TotalAmountFormat);
							if (d > 0m)
							{
								textBoxAmount.ReadOnly = true;
							}
						}
					}
				}
				else
				{
					ErrorHelper.InformationMessage("Please select a vendor.");
				}
			}
			catch (Exception e)
			{
				ErrorHelper.ProcessError(e);
			}
		}

		protected override void Dispose(bool disposing)
		{
			if (disposing && components != null)
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		private void InitializeComponent()
		{
			components = new System.ComponentModel.Container();
			Infragistics.Win.Appearance appearance = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance2 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance3 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance4 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance5 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance6 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance7 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance8 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance9 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance10 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance11 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance12 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance13 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance14 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance15 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance16 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance17 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance18 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance19 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance20 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance21 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance22 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance23 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance24 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance25 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance26 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance27 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance28 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance29 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance30 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance31 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance32 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance33 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance34 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance35 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance36 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance37 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance38 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance39 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance40 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance41 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance42 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance43 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance44 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance45 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance46 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance47 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance48 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance49 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance50 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance51 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance52 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance53 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance54 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance55 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance56 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance57 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance58 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance59 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance60 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance61 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance62 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance63 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance64 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance65 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance66 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance67 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance68 = new Infragistics.Win.Appearance();
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Micromind.ClientUI.WindowsForms.DataEntries.Accounts.TTPaymentForm));
			Infragistics.Win.Appearance appearance69 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance70 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance71 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance72 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance73 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance74 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance75 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance76 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance77 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance78 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance79 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance80 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance81 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance82 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance83 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance84 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance85 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance86 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance87 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance88 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance89 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance90 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance91 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance92 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance93 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance94 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance95 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance96 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance97 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance98 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance99 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance100 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance101 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance102 = new Infragistics.Win.Appearance();
			Infragistics.Win.UltraWinTabControl.UltraTab ultraTab = new Infragistics.Win.UltraWinTabControl.UltraTab();
			Infragistics.Win.UltraWinTabControl.UltraTab ultraTab2 = new Infragistics.Win.UltraWinTabControl.UltraTab();
			Infragistics.Win.Appearance appearance103 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance104 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance105 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance106 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance107 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance108 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance109 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance110 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance111 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance112 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance113 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance114 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance115 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance116 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance117 = new Infragistics.Win.Appearance();
			Infragistics.Win.Appearance appearance118 = new Infragistics.Win.Appearance();
			tabPageItems = new Infragistics.Win.UltraWinTabControl.UltraTabPageControl();
			ultraFormattedLinkLabel8 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			buttonSelectInvoice = new Micromind.UISupport.XPButton();
			mmLabel3 = new Micromind.UISupport.MMLabel();
			textBoxTotalDue = new Micromind.UISupport.AmountTextBox();
			line1 = new Micromind.UISupport.Line();
			labelBaseCurrency = new System.Windows.Forms.Label();
			textBoxTotalAmount = new Micromind.UISupport.AmountTextBox();
			mmLabel5 = new Micromind.UISupport.MMLabel();
			textBoxAmountBase = new Micromind.UISupport.AmountTextBox();
			textBoxTotalFees = new Micromind.UISupport.AmountTextBox();
			mmLabel4 = new Micromind.UISupport.MMLabel();
			labelAmountBase = new System.Windows.Forms.Label();
			labelVoided = new System.Windows.Forms.Label();
			textBox1 = new System.Windows.Forms.TextBox();
			comboBoxBankAccount = new Micromind.DataControls.BankAccountsComboBox();
			ultraFormattedLinkLabel3 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			payeeSelector1 = new Micromind.DataControls.PayeeSelector();
			label2 = new System.Windows.Forms.Label();
			textBoxPayeeName = new System.Windows.Forms.TextBox();
			label5 = new System.Windows.Forms.Label();
			textBoxBalance = new System.Windows.Forms.TextBox();
			ultraFormattedLinkLabel6 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			textBoxAmount = new Micromind.UISupport.AmountTextBox();
			textBoxRegBalance = new System.Windows.Forms.TextBox();
			label1 = new System.Windows.Forms.Label();
			labelAnalysis = new System.Windows.Forms.Label();
			textBoxRef1 = new System.Windows.Forms.TextBox();
			comboBoxAnalysis = new Micromind.DataControls.AnalysisComboBox();
			tabPageExpense = new Infragistics.Win.UltraWinTabControl.UltraTabPageControl();
			linkLabelTax = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			textBoxTaxAmount = new Micromind.UISupport.AmountTextBox();
			dataGridExpense = new Micromind.DataControls.DataEntryGrid();
			textBoxTotalExpense = new Micromind.UISupport.NumberTextBox();
			label8 = new System.Windows.Forms.Label();
			comboBoxGridExpenseCode = new Micromind.DataControls.ExpenseCodeComboBox();
			comboBoxGridCurrency = new Micromind.DataControls.CurrencyComboBox();
			toolStrip1 = new System.Windows.Forms.ToolStrip();
			toolStripButtonFirst = new System.Windows.Forms.ToolStripButton();
			toolStripButtonPrevious = new System.Windows.Forms.ToolStripButton();
			toolStripButtonNext = new System.Windows.Forms.ToolStripButton();
			toolStripButtonLast = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonOpenList = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			toolStripTextBoxFind = new System.Windows.Forms.ToolStripTextBox();
			toolStripButtonFind = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonAttach = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonPrint = new System.Windows.Forms.ToolStripButton();
			toolStripButtonPreview = new System.Windows.Forms.ToolStripButton();
			toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonDistribution = new System.Windows.Forms.ToolStripButton();
			toolStripDropDownButton1 = new System.Windows.Forms.ToolStripDropDownButton();
			saveAsDraftToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			loadDraftToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			toolStripButtonApproval = new System.Windows.Forms.ToolStripButton();
			toolStripLabelApproval = new System.Windows.Forms.ToolStripLabel();
			toolStripSeparatorApproval = new System.Windows.Forms.ToolStripSeparator();
			toolStripButtonInformation = new System.Windows.Forms.ToolStripButton();
			panelButtons = new System.Windows.Forms.Panel();
			buttonVoid = new Micromind.UISupport.XPButton();
			buttonDelete = new Micromind.UISupport.XPButton();
			buttonNew = new Micromind.UISupport.XPButton();
			linePanelDown = new Micromind.UISupport.Line();
			xpButton1 = new Micromind.UISupport.XPButton();
			buttonSave = new Micromind.UISupport.XPButton();
			textBoxVoucherNumber = new System.Windows.Forms.TextBox();
			textBoxNote = new System.Windows.Forms.TextBox();
			label3 = new System.Windows.Forms.Label();
			labelCurrency = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraFormattedLinkLabel2 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraFormattedLinkLabel5 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			ultraFormattedLinkLabel4 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			textBoxDescription = new System.Windows.Forms.TextBox();
			label4 = new System.Windows.Forms.Label();
			panelDetails = new System.Windows.Forms.Panel();
			buttonSelectRequest = new Micromind.UISupport.XPButton();
			ultraFormattedLinkLabel1 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			textBoxRequest = new System.Windows.Forms.TextBox();
			dateTimePickerDate = new Micromind.UISupport.flatDatePicker();
			comboBoxSysDoc = new Micromind.DataControls.SysDocComboBox();
			comboBoxCostCenter = new Micromind.DataControls.CostCenterComboBox();
			currencySelector = new Micromind.DataControls.CurrencySelector();
			mmLabel1 = new Micromind.UISupport.MMLabel();
			ultraTabControl1 = new Infragistics.Win.UltraWinTabControl.UltraTabControl();
			ultraTabSharedControlsPage1 = new Infragistics.Win.UltraWinTabControl.UltraTabSharedControlsPage();
			formManager = new Micromind.DataControls.FormManager();
			panelJobCC = new System.Windows.Forms.Panel();
			ultraFormattedLinkLabel7 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			comboBoxJob = new Micromind.DataControls.JobComboBox();
			ultraFormattedLinkLabel9 = new Infragistics.Win.FormattedLinkLabel.UltraFormattedLinkLabel();
			comboBoxCostCategory = new Micromind.DataControls.CostCategoryComboBox();
			tabPageItems.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxBankAccount).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxAnalysis).BeginInit();
			tabPageExpense.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)dataGridExpense).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxGridExpenseCode).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxGridCurrency).BeginInit();
			toolStrip1.SuspendLayout();
			panelButtons.SuspendLayout();
			panelDetails.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxSysDoc).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCenter).BeginInit();
			((System.ComponentModel.ISupportInitialize)ultraTabControl1).BeginInit();
			ultraTabControl1.SuspendLayout();
			panelJobCC.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxJob).BeginInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCategory).BeginInit();
			SuspendLayout();
			tabPageItems.Controls.Add(ultraFormattedLinkLabel8);
			tabPageItems.Controls.Add(buttonSelectInvoice);
			tabPageItems.Controls.Add(mmLabel3);
			tabPageItems.Controls.Add(textBoxTotalDue);
			tabPageItems.Controls.Add(line1);
			tabPageItems.Controls.Add(labelBaseCurrency);
			tabPageItems.Controls.Add(textBoxTotalAmount);
			tabPageItems.Controls.Add(mmLabel5);
			tabPageItems.Controls.Add(textBoxAmountBase);
			tabPageItems.Controls.Add(textBoxTotalFees);
			tabPageItems.Controls.Add(mmLabel4);
			tabPageItems.Controls.Add(labelAmountBase);
			tabPageItems.Controls.Add(labelVoided);
			tabPageItems.Controls.Add(textBox1);
			tabPageItems.Controls.Add(comboBoxBankAccount);
			tabPageItems.Controls.Add(ultraFormattedLinkLabel3);
			tabPageItems.Controls.Add(payeeSelector1);
			tabPageItems.Controls.Add(label2);
			tabPageItems.Controls.Add(textBoxPayeeName);
			tabPageItems.Controls.Add(label5);
			tabPageItems.Controls.Add(textBoxBalance);
			tabPageItems.Controls.Add(ultraFormattedLinkLabel6);
			tabPageItems.Controls.Add(textBoxAmount);
			tabPageItems.Controls.Add(textBoxRegBalance);
			tabPageItems.Controls.Add(label1);
			tabPageItems.Controls.Add(labelAnalysis);
			tabPageItems.Controls.Add(textBoxRef1);
			tabPageItems.Controls.Add(comboBoxAnalysis);
			tabPageItems.Location = new System.Drawing.Point(1, 23);
			tabPageItems.Name = "tabPageItems";
			tabPageItems.Size = new System.Drawing.Size(634, 280);
			appearance.FontData.BoldAsString = "True";
			appearance.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel8.Appearance = appearance;
			ultraFormattedLinkLabel8.AutoSize = true;
			ultraFormattedLinkLabel8.Location = new System.Drawing.Point(13, 76);
			ultraFormattedLinkLabel8.Name = "ultraFormattedLinkLabel8";
			ultraFormattedLinkLabel8.Size = new System.Drawing.Size(52, 15);
			ultraFormattedLinkLabel8.TabIndex = 161;
			ultraFormattedLinkLabel8.TabStop = true;
			ultraFormattedLinkLabel8.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel8.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel8.Value = "Amount:";
			appearance2.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel8.VisitedLinkAppearance = appearance2;
			ultraFormattedLinkLabel8.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel8_LinkClicked);
			buttonSelectInvoice.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSelectInvoice.BackColor = System.Drawing.Color.DarkGray;
			buttonSelectInvoice.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSelectInvoice.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSelectInvoice.Enabled = false;
			buttonSelectInvoice.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSelectInvoice.Location = new System.Drawing.Point(205, 73);
			buttonSelectInvoice.Name = "buttonSelectInvoice";
			buttonSelectInvoice.Size = new System.Drawing.Size(27, 21);
			buttonSelectInvoice.TabIndex = 12;
			buttonSelectInvoice.Text = "...";
			buttonSelectInvoice.UseVisualStyleBackColor = false;
			buttonSelectInvoice.Click += new System.EventHandler(buttonSelectInvoice_Click);
			mmLabel3.AutoSize = true;
			mmLabel3.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f);
			mmLabel3.IsFieldHeader = false;
			mmLabel3.IsRequired = false;
			mmLabel3.Location = new System.Drawing.Point(409, 102);
			mmLabel3.Name = "mmLabel3";
			mmLabel3.PenWidth = 1f;
			mmLabel3.ShowBorder = false;
			mmLabel3.Size = new System.Drawing.Size(67, 13);
			mmLabel3.TabIndex = 159;
			mmLabel3.Text = "Current Due:";
			textBoxTotalDue.AllowDecimal = true;
			textBoxTotalDue.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTotalDue.CustomReportFieldName = "";
			textBoxTotalDue.CustomReportKey = "";
			textBoxTotalDue.CustomReportValueType = 1;
			textBoxTotalDue.IsComboTextBox = false;
			textBoxTotalDue.IsModified = false;
			textBoxTotalDue.Location = new System.Drawing.Point(481, 98);
			textBoxTotalDue.MaxLength = 15;
			textBoxTotalDue.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxTotalDue.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxTotalDue.Name = "textBoxTotalDue";
			textBoxTotalDue.NullText = "0";
			textBoxTotalDue.ReadOnly = true;
			textBoxTotalDue.Size = new System.Drawing.Size(138, 20);
			textBoxTotalDue.TabIndex = 16;
			textBoxTotalDue.Text = "0.00";
			textBoxTotalDue.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxTotalDue.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			line1.BackColor = System.Drawing.Color.White;
			line1.DrawWidth = 1;
			line1.IsVertical = false;
			line1.LineBackColor = System.Drawing.Color.Black;
			line1.Location = new System.Drawing.Point(-3, 161);
			line1.Name = "line1";
			line1.Size = new System.Drawing.Size(291, 1);
			line1.TabIndex = 154;
			line1.TabStop = false;
			labelBaseCurrency.AutoSize = true;
			labelBaseCurrency.BackColor = System.Drawing.Color.Transparent;
			labelBaseCurrency.Location = new System.Drawing.Point(10, 145);
			labelBaseCurrency.Name = "labelBaseCurrency";
			labelBaseCurrency.Size = new System.Drawing.Size(79, 13);
			labelBaseCurrency.TabIndex = 17;
			labelBaseCurrency.Text = "Base Currency:";
			textBoxTotalAmount.AllowDecimal = true;
			textBoxTotalAmount.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTotalAmount.CustomReportFieldName = "";
			textBoxTotalAmount.CustomReportKey = "";
			textBoxTotalAmount.CustomReportValueType = 1;
			textBoxTotalAmount.IsComboTextBox = false;
			textBoxTotalAmount.IsModified = false;
			textBoxTotalAmount.Location = new System.Drawing.Point(101, 212);
			textBoxTotalAmount.MaxLength = 15;
			textBoxTotalAmount.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxTotalAmount.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxTotalAmount.Name = "textBoxTotalAmount";
			textBoxTotalAmount.NullText = "0";
			textBoxTotalAmount.ReadOnly = true;
			textBoxTotalAmount.Size = new System.Drawing.Size(111, 20);
			textBoxTotalAmount.TabIndex = 20;
			textBoxTotalAmount.Text = "0.00";
			textBoxTotalAmount.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxTotalAmount.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			mmLabel5.AutoSize = true;
			mmLabel5.BackColor = System.Drawing.Color.Transparent;
			mmLabel5.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel5.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f, System.Drawing.FontStyle.Bold);
			mmLabel5.IsFieldHeader = false;
			mmLabel5.IsRequired = true;
			mmLabel5.Location = new System.Drawing.Point(13, 215);
			mmLabel5.Name = "mmLabel5";
			mmLabel5.PenWidth = 1f;
			mmLabel5.ShowBorder = false;
			mmLabel5.Size = new System.Drawing.Size(86, 13);
			mmLabel5.TabIndex = 152;
			mmLabel5.Text = "Total Amount:";
			textBoxAmountBase.AllowDecimal = true;
			textBoxAmountBase.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxAmountBase.CustomReportFieldName = "";
			textBoxAmountBase.CustomReportKey = "";
			textBoxAmountBase.CustomReportValueType = 1;
			textBoxAmountBase.IsComboTextBox = false;
			textBoxAmountBase.IsModified = false;
			textBoxAmountBase.Location = new System.Drawing.Point(101, 168);
			textBoxAmountBase.MaxLength = 15;
			textBoxAmountBase.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxAmountBase.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxAmountBase.Name = "textBoxAmountBase";
			textBoxAmountBase.NullText = "0";
			textBoxAmountBase.ReadOnly = true;
			textBoxAmountBase.Size = new System.Drawing.Size(111, 20);
			textBoxAmountBase.TabIndex = 18;
			textBoxAmountBase.Text = "0.00";
			textBoxAmountBase.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxAmountBase.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			textBoxTotalFees.AllowDecimal = true;
			textBoxTotalFees.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTotalFees.CustomReportFieldName = "";
			textBoxTotalFees.CustomReportKey = "";
			textBoxTotalFees.CustomReportValueType = 1;
			textBoxTotalFees.IsComboTextBox = false;
			textBoxTotalFees.IsModified = false;
			textBoxTotalFees.Location = new System.Drawing.Point(101, 190);
			textBoxTotalFees.MaxLength = 15;
			textBoxTotalFees.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxTotalFees.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxTotalFees.Name = "textBoxTotalFees";
			textBoxTotalFees.NullText = "0";
			textBoxTotalFees.ReadOnly = true;
			textBoxTotalFees.Size = new System.Drawing.Size(111, 20);
			textBoxTotalFees.TabIndex = 19;
			textBoxTotalFees.Text = "0.00";
			textBoxTotalFees.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxTotalFees.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			mmLabel4.AutoSize = true;
			mmLabel4.BackColor = System.Drawing.Color.Transparent;
			mmLabel4.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel4.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f, System.Drawing.FontStyle.Bold);
			mmLabel4.IsFieldHeader = false;
			mmLabel4.IsRequired = true;
			mmLabel4.Location = new System.Drawing.Point(13, 193);
			mmLabel4.Name = "mmLabel4";
			mmLabel4.PenWidth = 1f;
			mmLabel4.ShowBorder = false;
			mmLabel4.Size = new System.Drawing.Size(38, 13);
			mmLabel4.TabIndex = 151;
			mmLabel4.Text = "Fees:";
			labelAmountBase.AutoSize = true;
			labelAmountBase.BackColor = System.Drawing.Color.Transparent;
			labelAmountBase.Location = new System.Drawing.Point(13, 171);
			labelAmountBase.Name = "labelAmountBase";
			labelAmountBase.Size = new System.Drawing.Size(46, 13);
			labelAmountBase.TabIndex = 150;
			labelAmountBase.Text = "Amount:";
			labelVoided.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right);
			labelVoided.BackColor = System.Drawing.Color.Transparent;
			labelVoided.Font = new System.Drawing.Font("Microsoft Sans Serif", 14f, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0);
			labelVoided.ForeColor = System.Drawing.Color.DarkRed;
			labelVoided.Location = new System.Drawing.Point(533, 247);
			labelVoided.Name = "labelVoided";
			labelVoided.Size = new System.Drawing.Size(91, 21);
			labelVoided.TabIndex = 117;
			labelVoided.Text = "VOIDED";
			labelVoided.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			labelVoided.Visible = false;
			labelVoided.Click += new System.EventHandler(labelVoided_Click);
			textBox1.BackColor = System.Drawing.Color.WhiteSmoke;
			textBox1.Location = new System.Drawing.Point(203, 14);
			textBox1.Name = "textBox1";
			textBox1.ReadOnly = true;
			textBox1.Size = new System.Drawing.Size(226, 20);
			textBox1.TabIndex = 7;
			textBox1.TabStop = false;
			comboBoxBankAccount.Assigned = false;
			comboBoxBankAccount.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxBankAccount.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxBankAccount.CustomReportFieldName = "";
			comboBoxBankAccount.CustomReportKey = "";
			comboBoxBankAccount.CustomReportValueType = 1;
			comboBoxBankAccount.DescriptionTextBox = null;
			appearance3.BackColor = System.Drawing.SystemColors.Window;
			appearance3.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxBankAccount.DisplayLayout.Appearance = appearance3;
			comboBoxBankAccount.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxBankAccount.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance4.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance4.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance4.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance4.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxBankAccount.DisplayLayout.GroupByBox.Appearance = appearance4;
			appearance5.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxBankAccount.DisplayLayout.GroupByBox.BandLabelAppearance = appearance5;
			comboBoxBankAccount.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance6.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance6.BackColor2 = System.Drawing.SystemColors.Control;
			appearance6.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance6.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxBankAccount.DisplayLayout.GroupByBox.PromptAppearance = appearance6;
			comboBoxBankAccount.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxBankAccount.DisplayLayout.MaxRowScrollRegions = 1;
			appearance7.BackColor = System.Drawing.SystemColors.Window;
			appearance7.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxBankAccount.DisplayLayout.Override.ActiveCellAppearance = appearance7;
			appearance8.BackColor = System.Drawing.SystemColors.Highlight;
			appearance8.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxBankAccount.DisplayLayout.Override.ActiveRowAppearance = appearance8;
			comboBoxBankAccount.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxBankAccount.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance9.BackColor = System.Drawing.SystemColors.Window;
			comboBoxBankAccount.DisplayLayout.Override.CardAreaAppearance = appearance9;
			appearance10.BorderColor = System.Drawing.Color.Silver;
			appearance10.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxBankAccount.DisplayLayout.Override.CellAppearance = appearance10;
			comboBoxBankAccount.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxBankAccount.DisplayLayout.Override.CellPadding = 0;
			appearance11.BackColor = System.Drawing.SystemColors.Control;
			appearance11.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance11.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance11.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance11.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxBankAccount.DisplayLayout.Override.GroupByRowAppearance = appearance11;
			appearance12.TextHAlignAsString = "Left";
			comboBoxBankAccount.DisplayLayout.Override.HeaderAppearance = appearance12;
			comboBoxBankAccount.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxBankAccount.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance13.BackColor = System.Drawing.SystemColors.Window;
			appearance13.BorderColor = System.Drawing.Color.Silver;
			comboBoxBankAccount.DisplayLayout.Override.RowAppearance = appearance13;
			comboBoxBankAccount.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance14.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxBankAccount.DisplayLayout.Override.TemplateAddRowAppearance = appearance14;
			comboBoxBankAccount.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxBankAccount.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxBankAccount.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxBankAccount.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxBankAccount.Editable = true;
			comboBoxBankAccount.FilterString = "";
			comboBoxBankAccount.HasAllAccount = false;
			comboBoxBankAccount.HasCustom = false;
			comboBoxBankAccount.IsDataLoaded = false;
			comboBoxBankAccount.Location = new System.Drawing.Point(89, 14);
			comboBoxBankAccount.MaxDropDownItems = 12;
			comboBoxBankAccount.Name = "comboBoxBankAccount";
			comboBoxBankAccount.ShowInactiveItems = false;
			comboBoxBankAccount.ShowQuickAdd = true;
			comboBoxBankAccount.Size = new System.Drawing.Size(111, 20);
			comboBoxBankAccount.TabIndex = 6;
			comboBoxBankAccount.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			appearance15.BackColor = System.Drawing.Color.White;
			appearance15.FontData.BoldAsString = "True";
			appearance15.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel3.Appearance = appearance15;
			ultraFormattedLinkLabel3.AutoSize = true;
			ultraFormattedLinkLabel3.Location = new System.Drawing.Point(13, 54);
			ultraFormattedLinkLabel3.Name = "ultraFormattedLinkLabel3";
			ultraFormattedLinkLabel3.Size = new System.Drawing.Size(49, 15);
			ultraFormattedLinkLabel3.TabIndex = 112;
			ultraFormattedLinkLabel3.TabStop = true;
			ultraFormattedLinkLabel3.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel3.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel3.Value = "Paid To:";
			appearance16.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel3.VisitedLinkAppearance = appearance16;
			ultraFormattedLinkLabel3.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel3_LinkClicked);
			payeeSelector1.BackColor = System.Drawing.Color.Transparent;
			payeeSelector1.Location = new System.Drawing.Point(89, 52);
			payeeSelector1.MaximumSize = new System.Drawing.Size(2000, 20);
			payeeSelector1.MinimumSize = new System.Drawing.Size(0, 20);
			payeeSelector1.Name = "payeeSelector1";
			payeeSelector1.SelectedID = "";
			payeeSelector1.SelectedType = "";
			payeeSelector1.Size = new System.Drawing.Size(328, 20);
			payeeSelector1.TabIndex = 9;
			label2.AutoSize = true;
			label2.BackColor = System.Drawing.Color.Transparent;
			label2.Location = new System.Drawing.Point(433, 16);
			label2.Name = "label2";
			label2.Size = new System.Drawing.Size(49, 13);
			label2.TabIndex = 129;
			label2.Text = "Balance:";
			textBoxPayeeName.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxPayeeName.Location = new System.Drawing.Point(423, 52);
			textBoxPayeeName.Name = "textBoxPayeeName";
			textBoxPayeeName.ReadOnly = true;
			textBoxPayeeName.Size = new System.Drawing.Size(195, 20);
			textBoxPayeeName.TabIndex = 10;
			textBoxPayeeName.TabStop = false;
			label5.AutoSize = true;
			label5.BackColor = System.Drawing.Color.Transparent;
			label5.Location = new System.Drawing.Point(389, 78);
			label5.Name = "label5";
			label5.Size = new System.Drawing.Size(86, 13);
			label5.TabIndex = 129;
			label5.Text = "Current Balance:";
			textBoxBalance.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxBalance.Location = new System.Drawing.Point(480, 75);
			textBoxBalance.Name = "textBoxBalance";
			textBoxBalance.ReadOnly = true;
			textBoxBalance.Size = new System.Drawing.Size(138, 20);
			textBoxBalance.TabIndex = 13;
			textBoxBalance.TabStop = false;
			textBoxBalance.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			appearance17.BackColor = System.Drawing.Color.White;
			appearance17.FontData.BoldAsString = "True";
			appearance17.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel6.Appearance = appearance17;
			ultraFormattedLinkLabel6.AutoSize = true;
			ultraFormattedLinkLabel6.Location = new System.Drawing.Point(13, 16);
			ultraFormattedLinkLabel6.Name = "ultraFormattedLinkLabel6";
			ultraFormattedLinkLabel6.Size = new System.Drawing.Size(60, 15);
			ultraFormattedLinkLabel6.TabIndex = 121;
			ultraFormattedLinkLabel6.TabStop = true;
			ultraFormattedLinkLabel6.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel6.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel6.Value = "Pay From:";
			appearance18.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel6.VisitedLinkAppearance = appearance18;
			ultraFormattedLinkLabel6.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel6_LinkClicked);
			textBoxAmount.AllowDecimal = true;
			textBoxAmount.CustomReportFieldName = "";
			textBoxAmount.CustomReportKey = "";
			textBoxAmount.CustomReportValueType = 1;
			textBoxAmount.IsComboTextBox = false;
			textBoxAmount.IsModified = false;
			textBoxAmount.Location = new System.Drawing.Point(89, 74);
			textBoxAmount.MaxLength = 15;
			textBoxAmount.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxAmount.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxAmount.Name = "textBoxAmount";
			textBoxAmount.NullText = "0";
			textBoxAmount.Size = new System.Drawing.Size(114, 20);
			textBoxAmount.TabIndex = 11;
			textBoxAmount.Text = "0.00";
			textBoxAmount.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxAmount.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			textBoxRegBalance.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxRegBalance.Location = new System.Drawing.Point(485, 14);
			textBoxRegBalance.Name = "textBoxRegBalance";
			textBoxRegBalance.ReadOnly = true;
			textBoxRegBalance.Size = new System.Drawing.Size(133, 20);
			textBoxRegBalance.TabIndex = 8;
			textBoxRegBalance.TabStop = false;
			textBoxRegBalance.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			label1.AutoSize = true;
			label1.BackColor = System.Drawing.Color.Transparent;
			label1.Location = new System.Drawing.Point(12, 100);
			label1.Name = "label1";
			label1.Size = new System.Drawing.Size(60, 13);
			label1.TabIndex = 20;
			label1.Text = "Reference:";
			labelAnalysis.AutoSize = true;
			labelAnalysis.BackColor = System.Drawing.Color.Transparent;
			labelAnalysis.Location = new System.Drawing.Point(205, 100);
			labelAnalysis.Name = "labelAnalysis";
			labelAnalysis.Size = new System.Drawing.Size(48, 13);
			labelAnalysis.TabIndex = 119;
			labelAnalysis.Text = "Analysis:";
			labelAnalysis.Visible = false;
			textBoxRef1.Location = new System.Drawing.Point(89, 97);
			textBoxRef1.MaxLength = 15;
			textBoxRef1.Name = "textBoxRef1";
			textBoxRef1.Size = new System.Drawing.Size(114, 20);
			textBoxRef1.TabIndex = 14;
			comboBoxAnalysis.AlwaysInEditMode = true;
			comboBoxAnalysis.Assigned = false;
			comboBoxAnalysis.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxAnalysis.CustomReportFieldName = "";
			comboBoxAnalysis.CustomReportKey = "";
			comboBoxAnalysis.CustomReportValueType = 1;
			comboBoxAnalysis.DescriptionTextBox = null;
			appearance19.BackColor = System.Drawing.SystemColors.Window;
			appearance19.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxAnalysis.DisplayLayout.Appearance = appearance19;
			comboBoxAnalysis.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxAnalysis.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance20.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance20.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance20.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance20.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxAnalysis.DisplayLayout.GroupByBox.Appearance = appearance20;
			appearance21.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxAnalysis.DisplayLayout.GroupByBox.BandLabelAppearance = appearance21;
			comboBoxAnalysis.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance22.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance22.BackColor2 = System.Drawing.SystemColors.Control;
			appearance22.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance22.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxAnalysis.DisplayLayout.GroupByBox.PromptAppearance = appearance22;
			comboBoxAnalysis.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxAnalysis.DisplayLayout.MaxRowScrollRegions = 1;
			appearance23.BackColor = System.Drawing.SystemColors.Window;
			appearance23.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxAnalysis.DisplayLayout.Override.ActiveCellAppearance = appearance23;
			appearance24.BackColor = System.Drawing.SystemColors.Highlight;
			appearance24.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxAnalysis.DisplayLayout.Override.ActiveRowAppearance = appearance24;
			comboBoxAnalysis.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxAnalysis.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance25.BackColor = System.Drawing.SystemColors.Window;
			comboBoxAnalysis.DisplayLayout.Override.CardAreaAppearance = appearance25;
			appearance26.BorderColor = System.Drawing.Color.Silver;
			appearance26.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxAnalysis.DisplayLayout.Override.CellAppearance = appearance26;
			comboBoxAnalysis.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxAnalysis.DisplayLayout.Override.CellPadding = 0;
			appearance27.BackColor = System.Drawing.SystemColors.Control;
			appearance27.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance27.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance27.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance27.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxAnalysis.DisplayLayout.Override.GroupByRowAppearance = appearance27;
			appearance28.TextHAlignAsString = "Left";
			comboBoxAnalysis.DisplayLayout.Override.HeaderAppearance = appearance28;
			comboBoxAnalysis.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxAnalysis.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance29.BackColor = System.Drawing.SystemColors.Window;
			appearance29.BorderColor = System.Drawing.Color.Silver;
			comboBoxAnalysis.DisplayLayout.Override.RowAppearance = appearance29;
			comboBoxAnalysis.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance30.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxAnalysis.DisplayLayout.Override.TemplateAddRowAppearance = appearance30;
			comboBoxAnalysis.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxAnalysis.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxAnalysis.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxAnalysis.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxAnalysis.Editable = true;
			comboBoxAnalysis.FilterString = "";
			comboBoxAnalysis.HasAllAccount = false;
			comboBoxAnalysis.HasCustom = false;
			comboBoxAnalysis.IsDataLoaded = false;
			comboBoxAnalysis.Location = new System.Drawing.Point(260, 97);
			comboBoxAnalysis.MaxDropDownItems = 12;
			comboBoxAnalysis.Name = "comboBoxAnalysis";
			comboBoxAnalysis.ShowInactiveItems = false;
			comboBoxAnalysis.ShowQuickAdd = true;
			comboBoxAnalysis.Size = new System.Drawing.Size(136, 20);
			comboBoxAnalysis.TabIndex = 15;
			comboBoxAnalysis.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxAnalysis.Visible = false;
			tabPageExpense.Controls.Add(linkLabelTax);
			tabPageExpense.Controls.Add(textBoxTaxAmount);
			tabPageExpense.Controls.Add(dataGridExpense);
			tabPageExpense.Controls.Add(textBoxTotalExpense);
			tabPageExpense.Controls.Add(label8);
			tabPageExpense.Controls.Add(comboBoxGridExpenseCode);
			tabPageExpense.Controls.Add(comboBoxGridCurrency);
			tabPageExpense.Location = new System.Drawing.Point(-10000, -10000);
			tabPageExpense.Name = "tabPageExpense";
			tabPageExpense.Size = new System.Drawing.Size(634, 271);
			appearance31.FontData.BoldAsString = "False";
			appearance31.FontData.Name = "Tahoma";
			linkLabelTax.Appearance = appearance31;
			linkLabelTax.AutoSize = true;
			linkLabelTax.Location = new System.Drawing.Point(410, 254);
			linkLabelTax.Name = "linkLabelTax";
			linkLabelTax.Size = new System.Drawing.Size(25, 15);
			linkLabelTax.TabIndex = 166;
			linkLabelTax.TabStop = true;
			linkLabelTax.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			linkLabelTax.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			linkLabelTax.Value = "Tax:";
			linkLabelTax.Visible = false;
			appearance32.ForeColor = System.Drawing.Color.Blue;
			linkLabelTax.VisitedLinkAppearance = appearance32;
			textBoxTaxAmount.AllowDecimal = true;
			textBoxTaxAmount.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTaxAmount.CustomReportFieldName = "";
			textBoxTaxAmount.CustomReportKey = "";
			textBoxTaxAmount.CustomReportValueType = 1;
			textBoxTaxAmount.IsComboTextBox = false;
			textBoxTaxAmount.IsModified = false;
			textBoxTaxAmount.Location = new System.Drawing.Point(487, 251);
			textBoxTaxAmount.MaxLength = 15;
			textBoxTaxAmount.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxTaxAmount.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxTaxAmount.Name = "textBoxTaxAmount";
			textBoxTaxAmount.NullText = "0";
			textBoxTaxAmount.ReadOnly = true;
			textBoxTaxAmount.Size = new System.Drawing.Size(137, 20);
			textBoxTaxAmount.TabIndex = 165;
			textBoxTaxAmount.Text = "0.00";
			textBoxTaxAmount.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxTaxAmount.Value = new decimal(new int[4]
			{
				0,
				0,
				0,
				131072
			});
			textBoxTaxAmount.Visible = false;
			dataGridExpense.AllowAddNew = false;
			dataGridExpense.Anchor = (System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right);
			appearance33.BackColor = System.Drawing.SystemColors.Window;
			appearance33.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			dataGridExpense.DisplayLayout.Appearance = appearance33;
			dataGridExpense.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			dataGridExpense.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance34.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance34.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance34.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance34.BorderColor = System.Drawing.SystemColors.Window;
			dataGridExpense.DisplayLayout.GroupByBox.Appearance = appearance34;
			appearance35.ForeColor = System.Drawing.SystemColors.GrayText;
			dataGridExpense.DisplayLayout.GroupByBox.BandLabelAppearance = appearance35;
			dataGridExpense.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance36.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance36.BackColor2 = System.Drawing.SystemColors.Control;
			appearance36.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance36.ForeColor = System.Drawing.SystemColors.GrayText;
			dataGridExpense.DisplayLayout.GroupByBox.PromptAppearance = appearance36;
			dataGridExpense.DisplayLayout.MaxColScrollRegions = 1;
			dataGridExpense.DisplayLayout.MaxRowScrollRegions = 1;
			appearance37.BackColor = System.Drawing.SystemColors.Window;
			appearance37.ForeColor = System.Drawing.SystemColors.ControlText;
			dataGridExpense.DisplayLayout.Override.ActiveCellAppearance = appearance37;
			appearance38.BackColor = System.Drawing.SystemColors.Highlight;
			appearance38.ForeColor = System.Drawing.SystemColors.HighlightText;
			dataGridExpense.DisplayLayout.Override.ActiveRowAppearance = appearance38;
			dataGridExpense.DisplayLayout.Override.AllowAddNew = Infragistics.Win.UltraWinGrid.AllowAddNew.No;
			dataGridExpense.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			dataGridExpense.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance39.BackColor = System.Drawing.SystemColors.Window;
			dataGridExpense.DisplayLayout.Override.CardAreaAppearance = appearance39;
			appearance40.BorderColor = System.Drawing.Color.Silver;
			appearance40.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			dataGridExpense.DisplayLayout.Override.CellAppearance = appearance40;
			dataGridExpense.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			dataGridExpense.DisplayLayout.Override.CellPadding = 0;
			appearance41.BackColor = System.Drawing.SystemColors.Control;
			appearance41.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance41.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance41.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance41.BorderColor = System.Drawing.SystemColors.Window;
			dataGridExpense.DisplayLayout.Override.GroupByRowAppearance = appearance41;
			appearance42.TextHAlignAsString = "Left";
			dataGridExpense.DisplayLayout.Override.HeaderAppearance = appearance42;
			dataGridExpense.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			dataGridExpense.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance43.BackColor = System.Drawing.SystemColors.Window;
			appearance43.BorderColor = System.Drawing.Color.Silver;
			dataGridExpense.DisplayLayout.Override.RowAppearance = appearance43;
			dataGridExpense.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance44.BackColor = System.Drawing.SystemColors.ControlLight;
			dataGridExpense.DisplayLayout.Override.TemplateAddRowAppearance = appearance44;
			dataGridExpense.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			dataGridExpense.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			dataGridExpense.DisplayLayout.TabNavigation = Infragistics.Win.UltraWinGrid.TabNavigation.NextControlOnLastCell;
			dataGridExpense.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			dataGridExpense.ExitEditModeOnLeave = false;
			dataGridExpense.IncludeLotItems = false;
			dataGridExpense.LoadLayoutFailed = false;
			dataGridExpense.Location = new System.Drawing.Point(9, 9);
			dataGridExpense.MinimumSize = new System.Drawing.Size(450, 50);
			dataGridExpense.Name = "dataGridExpense";
			dataGridExpense.ShowClearMenu = true;
			dataGridExpense.ShowDeleteMenu = true;
			dataGridExpense.ShowInsertMenu = true;
			dataGridExpense.ShowMoveRowsMenu = true;
			dataGridExpense.Size = new System.Drawing.Size(615, 245);
			dataGridExpense.TabIndex = 2;
			dataGridExpense.Text = "dataEntryGrid1";
			dataGridExpense.AfterRowsDeleted += new System.EventHandler(dataGridExpense_AfterRowsDeleted);
			textBoxTotalExpense.AllowDecimal = true;
			textBoxTotalExpense.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right);
			textBoxTotalExpense.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxTotalExpense.CustomReportFieldName = "";
			textBoxTotalExpense.CustomReportKey = "";
			textBoxTotalExpense.CustomReportValueType = 1;
			textBoxTotalExpense.ForeColor = System.Drawing.Color.Black;
			textBoxTotalExpense.IsComboTextBox = false;
			textBoxTotalExpense.IsModified = false;
			textBoxTotalExpense.Location = new System.Drawing.Point(485, 234);
			textBoxTotalExpense.MaxValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				0
			});
			textBoxTotalExpense.MinValue = new decimal(new int[4]
			{
				-1,
				-1,
				-1,
				-2147483648
			});
			textBoxTotalExpense.Name = "textBoxTotalExpense";
			textBoxTotalExpense.NullText = "0";
			textBoxTotalExpense.ReadOnly = true;
			textBoxTotalExpense.Size = new System.Drawing.Size(139, 20);
			textBoxTotalExpense.TabIndex = 0;
			textBoxTotalExpense.TabStop = false;
			textBoxTotalExpense.Text = "0.00";
			textBoxTotalExpense.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			textBoxTotalExpense.Visible = false;
			label8.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right);
			label8.BackColor = System.Drawing.Color.Transparent;
			label8.Location = new System.Drawing.Point(6, 301);
			label8.Name = "label8";
			label8.Size = new System.Drawing.Size(471, 18);
			label8.TabIndex = 134;
			label8.Text = "Total Bank Fees:";
			label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			comboBoxGridExpenseCode.AlwaysInEditMode = true;
			comboBoxGridExpenseCode.Assigned = false;
			comboBoxGridExpenseCode.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxGridExpenseCode.CustomReportFieldName = "";
			comboBoxGridExpenseCode.CustomReportKey = "";
			comboBoxGridExpenseCode.CustomReportValueType = 1;
			comboBoxGridExpenseCode.DescriptionTextBox = null;
			appearance45.BackColor = System.Drawing.SystemColors.Window;
			appearance45.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxGridExpenseCode.DisplayLayout.Appearance = appearance45;
			comboBoxGridExpenseCode.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxGridExpenseCode.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance46.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance46.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance46.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance46.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxGridExpenseCode.DisplayLayout.GroupByBox.Appearance = appearance46;
			appearance47.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxGridExpenseCode.DisplayLayout.GroupByBox.BandLabelAppearance = appearance47;
			comboBoxGridExpenseCode.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance48.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance48.BackColor2 = System.Drawing.SystemColors.Control;
			appearance48.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance48.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxGridExpenseCode.DisplayLayout.GroupByBox.PromptAppearance = appearance48;
			comboBoxGridExpenseCode.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxGridExpenseCode.DisplayLayout.MaxRowScrollRegions = 1;
			appearance49.BackColor = System.Drawing.SystemColors.Window;
			appearance49.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxGridExpenseCode.DisplayLayout.Override.ActiveCellAppearance = appearance49;
			appearance50.BackColor = System.Drawing.SystemColors.Highlight;
			appearance50.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxGridExpenseCode.DisplayLayout.Override.ActiveRowAppearance = appearance50;
			comboBoxGridExpenseCode.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxGridExpenseCode.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance51.BackColor = System.Drawing.SystemColors.Window;
			comboBoxGridExpenseCode.DisplayLayout.Override.CardAreaAppearance = appearance51;
			appearance52.BorderColor = System.Drawing.Color.Silver;
			appearance52.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxGridExpenseCode.DisplayLayout.Override.CellAppearance = appearance52;
			comboBoxGridExpenseCode.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxGridExpenseCode.DisplayLayout.Override.CellPadding = 0;
			appearance53.BackColor = System.Drawing.SystemColors.Control;
			appearance53.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance53.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance53.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance53.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxGridExpenseCode.DisplayLayout.Override.GroupByRowAppearance = appearance53;
			appearance54.TextHAlignAsString = "Left";
			comboBoxGridExpenseCode.DisplayLayout.Override.HeaderAppearance = appearance54;
			comboBoxGridExpenseCode.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxGridExpenseCode.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance55.BackColor = System.Drawing.SystemColors.Window;
			appearance55.BorderColor = System.Drawing.Color.Silver;
			comboBoxGridExpenseCode.DisplayLayout.Override.RowAppearance = appearance55;
			comboBoxGridExpenseCode.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance56.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxGridExpenseCode.DisplayLayout.Override.TemplateAddRowAppearance = appearance56;
			comboBoxGridExpenseCode.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxGridExpenseCode.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxGridExpenseCode.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxGridExpenseCode.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxGridExpenseCode.Editable = true;
			comboBoxGridExpenseCode.FilterString = "";
			comboBoxGridExpenseCode.HasAllAccount = false;
			comboBoxGridExpenseCode.HasCustom = false;
			comboBoxGridExpenseCode.IsDataLoaded = false;
			comboBoxGridExpenseCode.Location = new System.Drawing.Point(557, 40);
			comboBoxGridExpenseCode.MaxDropDownItems = 12;
			comboBoxGridExpenseCode.Name = "comboBoxGridExpenseCode";
			comboBoxGridExpenseCode.ShowInactiveItems = false;
			comboBoxGridExpenseCode.ShowQuickAdd = true;
			comboBoxGridExpenseCode.Size = new System.Drawing.Size(124, 20);
			comboBoxGridExpenseCode.TabIndex = 121;
			comboBoxGridExpenseCode.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxGridExpenseCode.Visible = false;
			comboBoxGridCurrency.AlwaysInEditMode = true;
			comboBoxGridCurrency.Assigned = false;
			comboBoxGridCurrency.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxGridCurrency.CustomReportFieldName = "";
			comboBoxGridCurrency.CustomReportKey = "";
			comboBoxGridCurrency.CustomReportValueType = 1;
			comboBoxGridCurrency.DescriptionTextBox = null;
			appearance57.BackColor = System.Drawing.SystemColors.Window;
			appearance57.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxGridCurrency.DisplayLayout.Appearance = appearance57;
			comboBoxGridCurrency.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxGridCurrency.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance58.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance58.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance58.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance58.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxGridCurrency.DisplayLayout.GroupByBox.Appearance = appearance58;
			appearance59.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxGridCurrency.DisplayLayout.GroupByBox.BandLabelAppearance = appearance59;
			comboBoxGridCurrency.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance60.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance60.BackColor2 = System.Drawing.SystemColors.Control;
			appearance60.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance60.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxGridCurrency.DisplayLayout.GroupByBox.PromptAppearance = appearance60;
			comboBoxGridCurrency.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxGridCurrency.DisplayLayout.MaxRowScrollRegions = 1;
			appearance61.BackColor = System.Drawing.SystemColors.Window;
			appearance61.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxGridCurrency.DisplayLayout.Override.ActiveCellAppearance = appearance61;
			appearance62.BackColor = System.Drawing.SystemColors.Highlight;
			appearance62.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxGridCurrency.DisplayLayout.Override.ActiveRowAppearance = appearance62;
			comboBoxGridCurrency.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxGridCurrency.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance63.BackColor = System.Drawing.SystemColors.Window;
			comboBoxGridCurrency.DisplayLayout.Override.CardAreaAppearance = appearance63;
			appearance64.BorderColor = System.Drawing.Color.Silver;
			appearance64.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxGridCurrency.DisplayLayout.Override.CellAppearance = appearance64;
			comboBoxGridCurrency.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxGridCurrency.DisplayLayout.Override.CellPadding = 0;
			appearance65.BackColor = System.Drawing.SystemColors.Control;
			appearance65.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance65.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance65.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance65.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxGridCurrency.DisplayLayout.Override.GroupByRowAppearance = appearance65;
			appearance66.TextHAlignAsString = "Left";
			comboBoxGridCurrency.DisplayLayout.Override.HeaderAppearance = appearance66;
			comboBoxGridCurrency.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxGridCurrency.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance67.BackColor = System.Drawing.SystemColors.Window;
			appearance67.BorderColor = System.Drawing.Color.Silver;
			comboBoxGridCurrency.DisplayLayout.Override.RowAppearance = appearance67;
			comboBoxGridCurrency.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance68.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxGridCurrency.DisplayLayout.Override.TemplateAddRowAppearance = appearance68;
			comboBoxGridCurrency.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxGridCurrency.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxGridCurrency.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxGridCurrency.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxGridCurrency.Editable = true;
			comboBoxGridCurrency.FilterString = "";
			comboBoxGridCurrency.HasAllAccount = false;
			comboBoxGridCurrency.HasCustom = false;
			comboBoxGridCurrency.IsDataLoaded = false;
			comboBoxGridCurrency.Location = new System.Drawing.Point(350, 104);
			comboBoxGridCurrency.MaxDropDownItems = 12;
			comboBoxGridCurrency.Name = "comboBoxGridCurrency";
			comboBoxGridCurrency.ShowInactiveItems = false;
			comboBoxGridCurrency.ShowQuickAdd = true;
			comboBoxGridCurrency.Size = new System.Drawing.Size(95, 20);
			comboBoxGridCurrency.TabIndex = 122;
			comboBoxGridCurrency.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxGridCurrency.Visible = false;
			toolStrip1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden;
			toolStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
			toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[21]
			{
				toolStripButtonFirst,
				toolStripButtonPrevious,
				toolStripButtonNext,
				toolStripButtonLast,
				toolStripSeparator3,
				toolStripButtonOpenList,
				toolStripSeparator1,
				toolStripTextBoxFind,
				toolStripButtonFind,
				toolStripSeparator2,
				toolStripButtonAttach,
				toolStripSeparator4,
				toolStripButtonPrint,
				toolStripButtonPreview,
				toolStripSeparator5,
				toolStripButtonDistribution,
				toolStripDropDownButton1,
				toolStripButtonApproval,
				toolStripLabelApproval,
				toolStripSeparatorApproval,
				toolStripButtonInformation
			});
			toolStrip1.Location = new System.Drawing.Point(0, 0);
			toolStrip1.Name = "toolStrip1";
			toolStrip1.Size = new System.Drawing.Size(656, 31);
			toolStrip1.TabIndex = 0;
			toolStrip1.Text = "toolStrip1";
			toolStripButtonFirst.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonFirst.Image = Micromind.ClientUI.Properties.Resources.first;
			toolStripButtonFirst.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonFirst.Name = "toolStripButtonFirst";
			toolStripButtonFirst.Size = new System.Drawing.Size(28, 28);
			toolStripButtonFirst.Text = "First Record";
			toolStripButtonFirst.Click += new System.EventHandler(toolStripButtonFirst_Click);
			toolStripButtonPrevious.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonPrevious.Image = Micromind.ClientUI.Properties.Resources.prev;
			toolStripButtonPrevious.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonPrevious.Name = "toolStripButtonPrevious";
			toolStripButtonPrevious.Size = new System.Drawing.Size(28, 28);
			toolStripButtonPrevious.Text = "Previous Record";
			toolStripButtonPrevious.Click += new System.EventHandler(toolStripButtonPrevious_Click);
			toolStripButtonNext.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonNext.Image = Micromind.ClientUI.Properties.Resources.next;
			toolStripButtonNext.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonNext.Name = "toolStripButtonNext";
			toolStripButtonNext.Size = new System.Drawing.Size(28, 28);
			toolStripButtonNext.Text = "Next Record";
			toolStripButtonNext.Click += new System.EventHandler(toolStripButtonNext_Click);
			toolStripButtonLast.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonLast.Image = Micromind.ClientUI.Properties.Resources.last;
			toolStripButtonLast.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonLast.Name = "toolStripButtonLast";
			toolStripButtonLast.Size = new System.Drawing.Size(28, 28);
			toolStripButtonLast.Text = "Last Record";
			toolStripButtonLast.Click += new System.EventHandler(toolStripButtonLast_Click);
			toolStripSeparator3.Name = "toolStripSeparator3";
			toolStripSeparator3.Size = new System.Drawing.Size(6, 31);
			toolStripButtonOpenList.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonOpenList.Image = Micromind.ClientUI.Properties.Resources.list;
			toolStripButtonOpenList.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonOpenList.Name = "toolStripButtonOpenList";
			toolStripButtonOpenList.Size = new System.Drawing.Size(28, 28);
			toolStripButtonOpenList.Text = "Open List";
			toolStripButtonOpenList.Click += new System.EventHandler(toolStripButtonOpenList_Click);
			toolStripSeparator1.Name = "toolStripSeparator1";
			toolStripSeparator1.Size = new System.Drawing.Size(6, 31);
			toolStripTextBoxFind.Name = "toolStripTextBoxFind";
			toolStripTextBoxFind.Size = new System.Drawing.Size(100, 31);
			toolStripTextBoxFind.KeyPress += new System.Windows.Forms.KeyPressEventHandler(toolStripTextBoxFind_KeyPress);
			toolStripButtonFind.Image = Micromind.ClientUI.Properties.Resources.find;
			toolStripButtonFind.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonFind.Name = "toolStripButtonFind";
			toolStripButtonFind.Size = new System.Drawing.Size(58, 28);
			toolStripButtonFind.Text = "Find";
			toolStripButtonFind.Click += new System.EventHandler(toolStripButtonFind_Click);
			toolStripSeparator2.Name = "toolStripSeparator2";
			toolStripSeparator2.Size = new System.Drawing.Size(6, 31);
			toolStripButtonAttach.Image = Micromind.ClientUI.Properties.Resources.attach_24x24;
			toolStripButtonAttach.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonAttach.Name = "toolStripButtonAttach";
			toolStripButtonAttach.Size = new System.Drawing.Size(91, 28);
			toolStripButtonAttach.Text = "Attach File";
			toolStripButtonAttach.Click += new System.EventHandler(toolStripButtonAttach_Click);
			toolStripSeparator4.Name = "toolStripSeparator4";
			toolStripSeparator4.Size = new System.Drawing.Size(6, 31);
			toolStripButtonPrint.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonPrint.Image = Micromind.ClientUI.Properties.Resources.printer;
			toolStripButtonPrint.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonPrint.Name = "toolStripButtonPrint";
			toolStripButtonPrint.Size = new System.Drawing.Size(28, 28);
			toolStripButtonPrint.Text = "&Print";
			toolStripButtonPrint.ToolTipText = "Print (Ctrl+P)";
			toolStripButtonPrint.Click += new System.EventHandler(toolStripButtonPrint_Click);
			toolStripButtonPreview.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonPreview.Image = Micromind.ClientUI.Properties.Resources.preview;
			toolStripButtonPreview.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonPreview.Name = "toolStripButtonPreview";
			toolStripButtonPreview.Size = new System.Drawing.Size(28, 28);
			toolStripButtonPreview.Text = "Preview";
			toolStripButtonPreview.ToolTipText = "Preview";
			toolStripButtonPreview.Click += new System.EventHandler(toolStripButtonPreview_Click);
			toolStripSeparator5.Name = "toolStripSeparator5";
			toolStripSeparator5.Size = new System.Drawing.Size(6, 31);
			toolStripButtonDistribution.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonDistribution.Image = Micromind.ClientUI.Properties.Resources.jvdistribution;
			toolStripButtonDistribution.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonDistribution.Name = "toolStripButtonDistribution";
			toolStripButtonDistribution.Size = new System.Drawing.Size(28, 28);
			toolStripButtonDistribution.Text = "Journal Distribution Summary";
			toolStripButtonDistribution.Click += new System.EventHandler(toolStripButtonDistribution_Click);
			toolStripDropDownButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
			toolStripDropDownButton1.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[2]
			{
				saveAsDraftToolStripMenuItem,
				loadDraftToolStripMenuItem
			});
			toolStripDropDownButton1.Image = (System.Drawing.Image)resources.GetObject("toolStripDropDownButton1.Image");
			toolStripDropDownButton1.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripDropDownButton1.Name = "toolStripDropDownButton1";
			toolStripDropDownButton1.Size = new System.Drawing.Size(60, 28);
			toolStripDropDownButton1.Text = "Actions";
			saveAsDraftToolStripMenuItem.Name = "saveAsDraftToolStripMenuItem";
			saveAsDraftToolStripMenuItem.Size = new System.Drawing.Size(141, 22);
			saveAsDraftToolStripMenuItem.Text = "Save as Draft";
			saveAsDraftToolStripMenuItem.Click += new System.EventHandler(saveAsDraftToolStripMenuItem_Click);
			loadDraftToolStripMenuItem.Name = "loadDraftToolStripMenuItem";
			loadDraftToolStripMenuItem.Size = new System.Drawing.Size(141, 22);
			loadDraftToolStripMenuItem.Text = "Load Draft";
			loadDraftToolStripMenuItem.Click += new System.EventHandler(loadDraftToolStripMenuItem_Click);
			toolStripButtonApproval.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			toolStripButtonApproval.AutoSize = false;
			toolStripButtonApproval.BackColor = System.Drawing.Color.Transparent;
			toolStripButtonApproval.Font = new System.Drawing.Font("Segoe UI", 9f, System.Drawing.FontStyle.Bold);
			toolStripButtonApproval.ForeColor = System.Drawing.Color.Green;
			toolStripButtonApproval.ImageScaling = System.Windows.Forms.ToolStripItemImageScaling.None;
			toolStripButtonApproval.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonApproval.Name = "toolStripButtonApproval";
			toolStripButtonApproval.Overflow = System.Windows.Forms.ToolStripItemOverflow.Never;
			toolStripButtonApproval.Size = new System.Drawing.Size(70, 22);
			toolStripButtonApproval.Text = "Pending";
			toolStripLabelApproval.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			toolStripLabelApproval.Font = new System.Drawing.Font("Segoe UI", 9f, System.Drawing.FontStyle.Bold);
			toolStripLabelApproval.Name = "toolStripLabelApproval";
			toolStripLabelApproval.Size = new System.Drawing.Size(45, 15);
			toolStripLabelApproval.Text = "Status:";
			toolStripSeparatorApproval.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			toolStripSeparatorApproval.Name = "toolStripSeparatorApproval";
			toolStripSeparatorApproval.Size = new System.Drawing.Size(6, 25);
			toolStripButtonInformation.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
			toolStripButtonInformation.Image = Micromind.ClientUI.Properties.Resources.docinfo_24x24;
			toolStripButtonInformation.ImageTransparentColor = System.Drawing.Color.Magenta;
			toolStripButtonInformation.Name = "toolStripButtonInformation";
			toolStripButtonInformation.Size = new System.Drawing.Size(28, 28);
			toolStripButtonInformation.Text = "Document Information";
			toolStripButtonInformation.Click += new System.EventHandler(toolStripButtonInformation_Click);
			panelButtons.Controls.Add(buttonVoid);
			panelButtons.Controls.Add(buttonDelete);
			panelButtons.Controls.Add(buttonNew);
			panelButtons.Controls.Add(linePanelDown);
			panelButtons.Controls.Add(xpButton1);
			panelButtons.Controls.Add(buttonSave);
			panelButtons.Dock = System.Windows.Forms.DockStyle.Bottom;
			panelButtons.Location = new System.Drawing.Point(0, 473);
			panelButtons.Name = "panelButtons";
			panelButtons.Size = new System.Drawing.Size(656, 40);
			panelButtons.TabIndex = 1;
			buttonVoid.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonVoid.BackColor = System.Drawing.Color.DarkGray;
			buttonVoid.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonVoid.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonVoid.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			buttonVoid.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonVoid.Location = new System.Drawing.Point(216, 8);
			buttonVoid.Name = "buttonVoid";
			buttonVoid.Size = new System.Drawing.Size(96, 24);
			buttonVoid.TabIndex = 2;
			buttonVoid.Text = "&Void";
			buttonVoid.UseVisualStyleBackColor = false;
			buttonVoid.Click += new System.EventHandler(buttonVoid_Click);
			buttonDelete.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonDelete.BackColor = System.Drawing.Color.DarkGray;
			buttonDelete.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonDelete.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonDelete.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			buttonDelete.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonDelete.Location = new System.Drawing.Point(318, 8);
			buttonDelete.Name = "buttonDelete";
			buttonDelete.Size = new System.Drawing.Size(96, 24);
			buttonDelete.TabIndex = 3;
			buttonDelete.Text = "De&lete";
			buttonDelete.UseVisualStyleBackColor = false;
			buttonDelete.Click += new System.EventHandler(buttonDelete_Click);
			buttonNew.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonNew.BackColor = System.Drawing.Color.DarkGray;
			buttonNew.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonNew.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonNew.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonNew.Location = new System.Drawing.Point(114, 8);
			buttonNew.Name = "buttonNew";
			buttonNew.Size = new System.Drawing.Size(96, 24);
			buttonNew.TabIndex = 1;
			buttonNew.Text = "Ne&w...";
			buttonNew.UseVisualStyleBackColor = false;
			buttonNew.Click += new System.EventHandler(buttonNew_Click);
			linePanelDown.BackColor = System.Drawing.Color.White;
			linePanelDown.Dock = System.Windows.Forms.DockStyle.Top;
			linePanelDown.DrawWidth = 1;
			linePanelDown.IsVertical = false;
			linePanelDown.LineBackColor = System.Drawing.Color.Silver;
			linePanelDown.Location = new System.Drawing.Point(0, 0);
			linePanelDown.Name = "linePanelDown";
			linePanelDown.Size = new System.Drawing.Size(656, 1);
			linePanelDown.TabIndex = 14;
			linePanelDown.TabStop = false;
			xpButton1.AdjustImageLocation = new System.Drawing.Point(0, 0);
			xpButton1.Anchor = (System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right);
			xpButton1.BackColor = System.Drawing.Color.DarkGray;
			xpButton1.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			xpButton1.BtnStyle = Micromind.UISupport.XPStyle.Default;
			xpButton1.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			xpButton1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			xpButton1.Location = new System.Drawing.Point(551, 8);
			xpButton1.Name = "xpButton1";
			xpButton1.Size = new System.Drawing.Size(96, 24);
			xpButton1.TabIndex = 4;
			xpButton1.Text = "&Close";
			xpButton1.UseVisualStyleBackColor = false;
			xpButton1.Click += new System.EventHandler(xpButton1_Click);
			buttonSave.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSave.BackColor = System.Drawing.Color.Silver;
			buttonSave.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSave.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSave.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			buttonSave.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
			buttonSave.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSave.Location = new System.Drawing.Point(12, 8);
			buttonSave.Name = "buttonSave";
			buttonSave.Size = new System.Drawing.Size(96, 24);
			buttonSave.TabIndex = 0;
			buttonSave.Text = "&Save";
			buttonSave.UseVisualStyleBackColor = false;
			buttonSave.Click += new System.EventHandler(buttonSave_Click);
			textBoxVoucherNumber.Location = new System.Drawing.Point(298, 7);
			textBoxVoucherNumber.MaxLength = 15;
			textBoxVoucherNumber.Name = "textBoxVoucherNumber";
			textBoxVoucherNumber.Size = new System.Drawing.Size(111, 20);
			textBoxVoucherNumber.TabIndex = 1;
			textBoxNote.Location = new System.Drawing.Point(76, 75);
			textBoxNote.MaxLength = 255;
			textBoxNote.Name = "textBoxNote";
			textBoxNote.Size = new System.Drawing.Size(542, 20);
			textBoxNote.TabIndex = 8;
			label3.AutoSize = true;
			label3.Location = new System.Drawing.Point(-1, 78);
			label3.Name = "label3";
			label3.Size = new System.Drawing.Size(33, 13);
			label3.TabIndex = 20;
			label3.Text = "Note:";
			appearance69.FontData.BoldAsString = "False";
			labelCurrency.Appearance = appearance69;
			labelCurrency.AutoSize = true;
			labelCurrency.Location = new System.Drawing.Point(376, 32);
			labelCurrency.Name = "labelCurrency";
			labelCurrency.Size = new System.Drawing.Size(52, 14);
			labelCurrency.TabIndex = 4;
			labelCurrency.TabStop = true;
			labelCurrency.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			labelCurrency.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			labelCurrency.Value = "Currency:";
			appearance70.ForeColor = System.Drawing.Color.Blue;
			labelCurrency.VisitedLinkAppearance = appearance70;
			labelCurrency.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel1_LinkClicked);
			appearance71.FontData.BoldAsString = "True";
			appearance71.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel2.Appearance = appearance71;
			ultraFormattedLinkLabel2.AutoSize = true;
			ultraFormattedLinkLabel2.Location = new System.Drawing.Point(192, 9);
			ultraFormattedLinkLabel2.Name = "ultraFormattedLinkLabel2";
			ultraFormattedLinkLabel2.Size = new System.Drawing.Size(101, 15);
			ultraFormattedLinkLabel2.TabIndex = 1;
			ultraFormattedLinkLabel2.TabStop = true;
			ultraFormattedLinkLabel2.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel2.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel2.Value = "Voucher Number:";
			appearance72.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel2.VisitedLinkAppearance = appearance72;
			ultraFormattedLinkLabel2.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel2_LinkClicked);
			appearance73.FontData.BoldAsString = "True";
			appearance73.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel5.Appearance = appearance73;
			ultraFormattedLinkLabel5.AutoSize = true;
			ultraFormattedLinkLabel5.Location = new System.Drawing.Point(2, 9);
			ultraFormattedLinkLabel5.Name = "ultraFormattedLinkLabel5";
			ultraFormattedLinkLabel5.Size = new System.Drawing.Size(45, 15);
			ultraFormattedLinkLabel5.TabIndex = 116;
			ultraFormattedLinkLabel5.TabStop = true;
			ultraFormattedLinkLabel5.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel5.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel5.Value = "Doc ID:";
			appearance74.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel5.VisitedLinkAppearance = appearance74;
			ultraFormattedLinkLabel5.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel5_LinkClicked);
			appearance75.FontData.BoldAsString = "False";
			appearance75.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel4.Appearance = appearance75;
			ultraFormattedLinkLabel4.AutoSize = true;
			ultraFormattedLinkLabel4.Location = new System.Drawing.Point(0, 29);
			ultraFormattedLinkLabel4.Name = "ultraFormattedLinkLabel4";
			ultraFormattedLinkLabel4.Size = new System.Drawing.Size(65, 15);
			ultraFormattedLinkLabel4.TabIndex = 114;
			ultraFormattedLinkLabel4.TabStop = true;
			ultraFormattedLinkLabel4.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel4.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel4.Value = "Cost Center:";
			appearance76.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel4.VisitedLinkAppearance = appearance76;
			ultraFormattedLinkLabel4.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel4_LinkClicked);
			textBoxDescription.Location = new System.Drawing.Point(76, 53);
			textBoxDescription.MaxLength = 255;
			textBoxDescription.Name = "textBoxDescription";
			textBoxDescription.Size = new System.Drawing.Size(542, 20);
			textBoxDescription.TabIndex = 7;
			label4.AutoSize = true;
			label4.Location = new System.Drawing.Point(-1, 56);
			label4.Name = "label4";
			label4.Size = new System.Drawing.Size(49, 13);
			label4.TabIndex = 127;
			label4.Text = "Paid For:";
			panelDetails.Controls.Add(panelJobCC);
			panelDetails.Controls.Add(buttonSelectRequest);
			panelDetails.Controls.Add(ultraFormattedLinkLabel1);
			panelDetails.Controls.Add(textBoxRequest);
			panelDetails.Controls.Add(textBoxDescription);
			panelDetails.Controls.Add(label4);
			panelDetails.Controls.Add(dateTimePickerDate);
			panelDetails.Controls.Add(ultraFormattedLinkLabel5);
			panelDetails.Controls.Add(comboBoxSysDoc);
			panelDetails.Controls.Add(ultraFormattedLinkLabel4);
			panelDetails.Controls.Add(comboBoxCostCenter);
			panelDetails.Controls.Add(textBoxVoucherNumber);
			panelDetails.Controls.Add(ultraFormattedLinkLabel2);
			panelDetails.Controls.Add(labelCurrency);
			panelDetails.Controls.Add(textBoxNote);
			panelDetails.Controls.Add(currencySelector);
			panelDetails.Controls.Add(label3);
			panelDetails.Controls.Add(mmLabel1);
			panelDetails.Location = new System.Drawing.Point(10, 34);
			panelDetails.Name = "panelDetails";
			panelDetails.Size = new System.Drawing.Size(634, 126);
			panelDetails.TabIndex = 0;
			buttonSelectRequest.AdjustImageLocation = new System.Drawing.Point(0, 0);
			buttonSelectRequest.BackColor = System.Drawing.Color.DarkGray;
			buttonSelectRequest.BtnShape = Micromind.UISupport.BtnShape.Rectangle;
			buttonSelectRequest.BtnStyle = Micromind.UISupport.XPStyle.Default;
			buttonSelectRequest.ImeMode = System.Windows.Forms.ImeMode.NoControl;
			buttonSelectRequest.Location = new System.Drawing.Point(593, 7);
			buttonSelectRequest.Name = "buttonSelectRequest";
			buttonSelectRequest.Size = new System.Drawing.Size(26, 22);
			buttonSelectRequest.TabIndex = 3;
			buttonSelectRequest.Text = "...";
			buttonSelectRequest.UseVisualStyleBackColor = false;
			buttonSelectRequest.Click += new System.EventHandler(buttonSelectRequest_Click);
			appearance77.FontData.BoldAsString = "False";
			appearance77.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel1.Appearance = appearance77;
			ultraFormattedLinkLabel1.AutoSize = true;
			ultraFormattedLinkLabel1.Location = new System.Drawing.Point(418, 9);
			ultraFormattedLinkLabel1.Name = "ultraFormattedLinkLabel1";
			ultraFormattedLinkLabel1.Size = new System.Drawing.Size(48, 15);
			ultraFormattedLinkLabel1.TabIndex = 132;
			ultraFormattedLinkLabel1.TabStop = true;
			ultraFormattedLinkLabel1.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel1.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel1.Value = "Request:";
			appearance78.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel1.VisitedLinkAppearance = appearance78;
			ultraFormattedLinkLabel1.LinkClicked += new Infragistics.Win.FormattedLinkLabel.LinkClickedEventHandler(ultraFormattedLinkLabel1_LinkClicked_1);
			textBoxRequest.BackColor = System.Drawing.Color.WhiteSmoke;
			textBoxRequest.Location = new System.Drawing.Point(472, 7);
			textBoxRequest.Name = "textBoxRequest";
			textBoxRequest.ReadOnly = true;
			textBoxRequest.Size = new System.Drawing.Size(119, 20);
			textBoxRequest.TabIndex = 2;
			textBoxRequest.TabStop = false;
			dateTimePickerDate.Format = System.Windows.Forms.DateTimePickerFormat.Short;
			dateTimePickerDate.Location = new System.Drawing.Point(239, 29);
			dateTimePickerDate.Name = "dateTimePickerDate";
			dateTimePickerDate.Size = new System.Drawing.Size(133, 20);
			dateTimePickerDate.TabIndex = 5;
			dateTimePickerDate.Value = new System.DateTime(2008, 5, 15, 11, 57, 9, 732);
			comboBoxSysDoc.AlwaysInEditMode = true;
			comboBoxSysDoc.Assigned = false;
			comboBoxSysDoc.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxSysDoc.CustomReportFieldName = "";
			comboBoxSysDoc.CustomReportKey = "";
			comboBoxSysDoc.CustomReportValueType = 1;
			comboBoxSysDoc.DescriptionTextBox = null;
			appearance79.BackColor = System.Drawing.SystemColors.Window;
			appearance79.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxSysDoc.DisplayLayout.Appearance = appearance79;
			comboBoxSysDoc.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxSysDoc.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance80.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance80.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance80.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance80.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.GroupByBox.Appearance = appearance80;
			appearance81.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxSysDoc.DisplayLayout.GroupByBox.BandLabelAppearance = appearance81;
			comboBoxSysDoc.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance82.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance82.BackColor2 = System.Drawing.SystemColors.Control;
			appearance82.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance82.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxSysDoc.DisplayLayout.GroupByBox.PromptAppearance = appearance82;
			comboBoxSysDoc.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxSysDoc.DisplayLayout.MaxRowScrollRegions = 1;
			appearance83.BackColor = System.Drawing.SystemColors.Window;
			appearance83.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxSysDoc.DisplayLayout.Override.ActiveCellAppearance = appearance83;
			appearance84.BackColor = System.Drawing.SystemColors.Highlight;
			appearance84.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxSysDoc.DisplayLayout.Override.ActiveRowAppearance = appearance84;
			comboBoxSysDoc.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxSysDoc.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance85.BackColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.Override.CardAreaAppearance = appearance85;
			appearance86.BorderColor = System.Drawing.Color.Silver;
			appearance86.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxSysDoc.DisplayLayout.Override.CellAppearance = appearance86;
			comboBoxSysDoc.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxSysDoc.DisplayLayout.Override.CellPadding = 0;
			appearance87.BackColor = System.Drawing.SystemColors.Control;
			appearance87.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance87.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance87.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance87.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxSysDoc.DisplayLayout.Override.GroupByRowAppearance = appearance87;
			appearance88.TextHAlignAsString = "Left";
			comboBoxSysDoc.DisplayLayout.Override.HeaderAppearance = appearance88;
			comboBoxSysDoc.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxSysDoc.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance89.BackColor = System.Drawing.SystemColors.Window;
			appearance89.BorderColor = System.Drawing.Color.Silver;
			comboBoxSysDoc.DisplayLayout.Override.RowAppearance = appearance89;
			comboBoxSysDoc.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance90.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxSysDoc.DisplayLayout.Override.TemplateAddRowAppearance = appearance90;
			comboBoxSysDoc.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxSysDoc.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxSysDoc.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxSysDoc.DivisionID = "";
			comboBoxSysDoc.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxSysDoc.DropDownStyle = Infragistics.Win.UltraWinGrid.UltraComboStyle.DropDownList;
			comboBoxSysDoc.Editable = true;
			comboBoxSysDoc.ExcludeFromSecurity = false;
			comboBoxSysDoc.FilterString = "";
			comboBoxSysDoc.HasAllAccount = false;
			comboBoxSysDoc.HasCustom = false;
			comboBoxSysDoc.IsDataLoaded = false;
			comboBoxSysDoc.Location = new System.Drawing.Point(76, 7);
			comboBoxSysDoc.MaxDropDownItems = 12;
			comboBoxSysDoc.Name = "comboBoxSysDoc";
			comboBoxSysDoc.ShowAll = false;
			comboBoxSysDoc.ShowInactiveItems = false;
			comboBoxSysDoc.ShowQuickAdd = true;
			comboBoxSysDoc.Size = new System.Drawing.Size(111, 20);
			comboBoxSysDoc.TabIndex = 0;
			comboBoxSysDoc.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			comboBoxCostCenter.AlwaysInEditMode = true;
			comboBoxCostCenter.Assigned = false;
			comboBoxCostCenter.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxCostCenter.CustomReportFieldName = "";
			comboBoxCostCenter.CustomReportKey = "";
			comboBoxCostCenter.CustomReportValueType = 1;
			comboBoxCostCenter.DescriptionTextBox = null;
			appearance91.BackColor = System.Drawing.SystemColors.Window;
			appearance91.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxCostCenter.DisplayLayout.Appearance = appearance91;
			comboBoxCostCenter.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxCostCenter.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance92.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance92.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance92.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance92.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.GroupByBox.Appearance = appearance92;
			appearance93.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCenter.DisplayLayout.GroupByBox.BandLabelAppearance = appearance93;
			comboBoxCostCenter.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance94.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance94.BackColor2 = System.Drawing.SystemColors.Control;
			appearance94.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance94.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCenter.DisplayLayout.GroupByBox.PromptAppearance = appearance94;
			comboBoxCostCenter.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxCostCenter.DisplayLayout.MaxRowScrollRegions = 1;
			appearance95.BackColor = System.Drawing.SystemColors.Window;
			appearance95.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxCostCenter.DisplayLayout.Override.ActiveCellAppearance = appearance95;
			appearance96.BackColor = System.Drawing.SystemColors.Highlight;
			appearance96.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxCostCenter.DisplayLayout.Override.ActiveRowAppearance = appearance96;
			comboBoxCostCenter.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxCostCenter.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance97.BackColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.Override.CardAreaAppearance = appearance97;
			appearance98.BorderColor = System.Drawing.Color.Silver;
			appearance98.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxCostCenter.DisplayLayout.Override.CellAppearance = appearance98;
			comboBoxCostCenter.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxCostCenter.DisplayLayout.Override.CellPadding = 0;
			appearance99.BackColor = System.Drawing.SystemColors.Control;
			appearance99.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance99.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance99.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance99.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCenter.DisplayLayout.Override.GroupByRowAppearance = appearance99;
			appearance100.TextHAlignAsString = "Left";
			comboBoxCostCenter.DisplayLayout.Override.HeaderAppearance = appearance100;
			comboBoxCostCenter.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxCostCenter.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance101.BackColor = System.Drawing.SystemColors.Window;
			appearance101.BorderColor = System.Drawing.Color.Silver;
			comboBoxCostCenter.DisplayLayout.Override.RowAppearance = appearance101;
			comboBoxCostCenter.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance102.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxCostCenter.DisplayLayout.Override.TemplateAddRowAppearance = appearance102;
			comboBoxCostCenter.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxCostCenter.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxCostCenter.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxCostCenter.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxCostCenter.Editable = true;
			comboBoxCostCenter.FilterString = "";
			comboBoxCostCenter.HasAllAccount = false;
			comboBoxCostCenter.HasCustom = false;
			comboBoxCostCenter.IsDataLoaded = false;
			comboBoxCostCenter.Location = new System.Drawing.Point(76, 29);
			comboBoxCostCenter.MaxDropDownItems = 12;
			comboBoxCostCenter.Name = "comboBoxCostCenter";
			comboBoxCostCenter.ShowInactiveItems = false;
			comboBoxCostCenter.ShowQuickAdd = true;
			comboBoxCostCenter.Size = new System.Drawing.Size(111, 20);
			comboBoxCostCenter.TabIndex = 4;
			comboBoxCostCenter.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			currencySelector.BackColor = System.Drawing.Color.WhiteSmoke;
			currencySelector.Location = new System.Drawing.Point(431, 29);
			currencySelector.MaximumSize = new System.Drawing.Size(99999, 20);
			currencySelector.MinimumSize = new System.Drawing.Size(5, 20);
			currencySelector.Name = "currencySelector";
			currencySelector.Rate = new decimal(new int[4]
			{
				1,
				0,
				0,
				0
			});
			currencySelector.SelectedID = "";
			currencySelector.Size = new System.Drawing.Size(187, 20);
			currencySelector.TabIndex = 6;
			mmLabel1.AutoSize = true;
			mmLabel1.BorderColor = System.Drawing.Color.FromArgb(78, 122, 171);
			mmLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25f, System.Drawing.FontStyle.Bold);
			mmLabel1.IsFieldHeader = false;
			mmLabel1.IsRequired = true;
			mmLabel1.Location = new System.Drawing.Point(191, 30);
			mmLabel1.Name = "mmLabel1";
			mmLabel1.PenWidth = 1f;
			mmLabel1.ShowBorder = false;
			mmLabel1.Size = new System.Drawing.Size(38, 13);
			mmLabel1.TabIndex = 2;
			mmLabel1.Text = "Date:";
			ultraTabControl1.Anchor = (System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right);
			ultraTabControl1.Controls.Add(ultraTabSharedControlsPage1);
			ultraTabControl1.Controls.Add(tabPageItems);
			ultraTabControl1.Controls.Add(tabPageExpense);
			ultraTabControl1.Location = new System.Drawing.Point(9, 165);
			ultraTabControl1.Name = "ultraTabControl1";
			ultraTabControl1.SharedControlsPage = ultraTabSharedControlsPage1;
			ultraTabControl1.Size = new System.Drawing.Size(638, 306);
			ultraTabControl1.TabIndex = 17;
			ultraTab.TabPage = tabPageItems;
			ultraTab.Text = "Payment Details";
			ultraTab2.TabPage = tabPageExpense;
			ultraTab2.Text = "Bank Fees";
			ultraTabControl1.Tabs.AddRange(new Infragistics.Win.UltraWinTabControl.UltraTab[2]
			{
				ultraTab,
				ultraTab2
			});
			ultraTabSharedControlsPage1.Location = new System.Drawing.Point(-10000, -10000);
			ultraTabSharedControlsPage1.Name = "ultraTabSharedControlsPage1";
			ultraTabSharedControlsPage1.Size = new System.Drawing.Size(634, 280);
			formManager.BackColor = System.Drawing.Color.RosyBrown;
			formManager.Dock = System.Windows.Forms.DockStyle.Left;
			formManager.IsForcedDirty = false;
			formManager.Location = new System.Drawing.Point(0, 31);
			formManager.MaximumSize = new System.Drawing.Size(20, 20);
			formManager.MinimumSize = new System.Drawing.Size(20, 20);
			formManager.Name = "formManager";
			formManager.Size = new System.Drawing.Size(20, 20);
			formManager.TabIndex = 16;
			formManager.Text = "formManager1";
			formManager.Visible = false;
			panelJobCC.Controls.Add(ultraFormattedLinkLabel7);
			panelJobCC.Controls.Add(comboBoxJob);
			panelJobCC.Controls.Add(ultraFormattedLinkLabel9);
			panelJobCC.Controls.Add(comboBoxCostCategory);
			panelJobCC.Location = new System.Drawing.Point(2, 97);
			panelJobCC.Name = "panelJobCC";
			panelJobCC.Size = new System.Drawing.Size(407, 28);
			panelJobCC.TabIndex = 134;
			panelJobCC.Visible = false;
			appearance103.FontData.BoldAsString = "False";
			appearance103.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel7.Appearance = appearance103;
			ultraFormattedLinkLabel7.AutoSize = true;
			ultraFormattedLinkLabel7.Location = new System.Drawing.Point(192, 4);
			ultraFormattedLinkLabel7.Name = "ultraFormattedLinkLabel7";
			ultraFormattedLinkLabel7.Size = new System.Drawing.Size(76, 15);
			ultraFormattedLinkLabel7.TabIndex = 132;
			ultraFormattedLinkLabel7.TabStop = true;
			ultraFormattedLinkLabel7.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel7.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel7.Value = "Cost Category:";
			appearance104.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel7.VisitedLinkAppearance = appearance104;
			comboBoxJob.Assigned = false;
			comboBoxJob.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxJob.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxJob.CustomReportFieldName = "";
			comboBoxJob.CustomReportKey = "";
			comboBoxJob.CustomReportValueType = 1;
			comboBoxJob.DescriptionTextBox = null;
			comboBoxJob.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxJob.Editable = true;
			comboBoxJob.FilterString = "";
			comboBoxJob.HasAllAccount = false;
			comboBoxJob.HasCustom = false;
			comboBoxJob.IsDataLoaded = false;
			comboBoxJob.Location = new System.Drawing.Point(74, 2);
			comboBoxJob.MaxDropDownItems = 12;
			comboBoxJob.Name = "comboBoxJob";
			comboBoxJob.ShowInactiveItems = false;
			comboBoxJob.ShowQuickAdd = true;
			comboBoxJob.Size = new System.Drawing.Size(111, 20);
			comboBoxJob.TabIndex = 129;
			comboBoxJob.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			appearance105.FontData.BoldAsString = "False";
			appearance105.FontData.Name = "Tahoma";
			ultraFormattedLinkLabel9.Appearance = appearance105;
			ultraFormattedLinkLabel9.AutoSize = true;
			ultraFormattedLinkLabel9.Location = new System.Drawing.Point(-2, 4);
			ultraFormattedLinkLabel9.Name = "ultraFormattedLinkLabel9";
			ultraFormattedLinkLabel9.Size = new System.Drawing.Size(42, 15);
			ultraFormattedLinkLabel9.TabIndex = 131;
			ultraFormattedLinkLabel9.TabStop = true;
			ultraFormattedLinkLabel9.TreatValueAs = Infragistics.Win.FormattedLinkLabel.TreatValueAs.URL;
			ultraFormattedLinkLabel9.UnderlineLinks = Infragistics.Win.FormattedLinkLabel.UnderlineLink.WhenHovered;
			ultraFormattedLinkLabel9.Value = "Project:";
			appearance106.ForeColor = System.Drawing.Color.Blue;
			ultraFormattedLinkLabel9.VisitedLinkAppearance = appearance106;
			comboBoxCostCategory.Assigned = false;
			comboBoxCostCategory.AutoCompleteMode = Infragistics.Win.AutoCompleteMode.Append;
			comboBoxCostCategory.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
			comboBoxCostCategory.CustomReportFieldName = "";
			comboBoxCostCategory.CustomReportKey = "";
			comboBoxCostCategory.CustomReportValueType = 1;
			comboBoxCostCategory.DescriptionTextBox = null;
			appearance107.BackColor = System.Drawing.SystemColors.Window;
			appearance107.BorderColor = System.Drawing.SystemColors.InactiveCaption;
			comboBoxCostCategory.DisplayLayout.Appearance = appearance107;
			comboBoxCostCategory.DisplayLayout.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			comboBoxCostCategory.DisplayLayout.CaptionVisible = Infragistics.Win.DefaultableBoolean.False;
			appearance108.BackColor = System.Drawing.SystemColors.ActiveBorder;
			appearance108.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance108.BackGradientStyle = Infragistics.Win.GradientStyle.Vertical;
			appearance108.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCategory.DisplayLayout.GroupByBox.Appearance = appearance108;
			appearance109.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCategory.DisplayLayout.GroupByBox.BandLabelAppearance = appearance109;
			comboBoxCostCategory.DisplayLayout.GroupByBox.BorderStyle = Infragistics.Win.UIElementBorderStyle.Solid;
			appearance110.BackColor = System.Drawing.SystemColors.ControlLightLight;
			appearance110.BackColor2 = System.Drawing.SystemColors.Control;
			appearance110.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance110.ForeColor = System.Drawing.SystemColors.GrayText;
			comboBoxCostCategory.DisplayLayout.GroupByBox.PromptAppearance = appearance110;
			comboBoxCostCategory.DisplayLayout.MaxColScrollRegions = 1;
			comboBoxCostCategory.DisplayLayout.MaxRowScrollRegions = 1;
			appearance111.BackColor = System.Drawing.SystemColors.Window;
			appearance111.ForeColor = System.Drawing.SystemColors.ControlText;
			comboBoxCostCategory.DisplayLayout.Override.ActiveCellAppearance = appearance111;
			appearance112.BackColor = System.Drawing.SystemColors.Highlight;
			appearance112.ForeColor = System.Drawing.SystemColors.HighlightText;
			comboBoxCostCategory.DisplayLayout.Override.ActiveRowAppearance = appearance112;
			comboBoxCostCategory.DisplayLayout.Override.BorderStyleCell = Infragistics.Win.UIElementBorderStyle.Dotted;
			comboBoxCostCategory.DisplayLayout.Override.BorderStyleRow = Infragistics.Win.UIElementBorderStyle.Dotted;
			appearance113.BackColor = System.Drawing.SystemColors.Window;
			comboBoxCostCategory.DisplayLayout.Override.CardAreaAppearance = appearance113;
			appearance114.BorderColor = System.Drawing.Color.Silver;
			appearance114.TextTrimming = Infragistics.Win.TextTrimming.EllipsisCharacter;
			comboBoxCostCategory.DisplayLayout.Override.CellAppearance = appearance114;
			comboBoxCostCategory.DisplayLayout.Override.CellClickAction = Infragistics.Win.UltraWinGrid.CellClickAction.EditAndSelectText;
			comboBoxCostCategory.DisplayLayout.Override.CellPadding = 0;
			appearance115.BackColor = System.Drawing.SystemColors.Control;
			appearance115.BackColor2 = System.Drawing.SystemColors.ControlDark;
			appearance115.BackGradientAlignment = Infragistics.Win.GradientAlignment.Element;
			appearance115.BackGradientStyle = Infragistics.Win.GradientStyle.Horizontal;
			appearance115.BorderColor = System.Drawing.SystemColors.Window;
			comboBoxCostCategory.DisplayLayout.Override.GroupByRowAppearance = appearance115;
			appearance116.TextHAlignAsString = "Left";
			comboBoxCostCategory.DisplayLayout.Override.HeaderAppearance = appearance116;
			comboBoxCostCategory.DisplayLayout.Override.HeaderClickAction = Infragistics.Win.UltraWinGrid.HeaderClickAction.SortMulti;
			comboBoxCostCategory.DisplayLayout.Override.HeaderStyle = Infragistics.Win.HeaderStyle.WindowsXPCommand;
			appearance117.BackColor = System.Drawing.SystemColors.Window;
			appearance117.BorderColor = System.Drawing.Color.Silver;
			comboBoxCostCategory.DisplayLayout.Override.RowAppearance = appearance117;
			comboBoxCostCategory.DisplayLayout.Override.RowSelectors = Infragistics.Win.DefaultableBoolean.False;
			appearance118.BackColor = System.Drawing.SystemColors.ControlLight;
			comboBoxCostCategory.DisplayLayout.Override.TemplateAddRowAppearance = appearance118;
			comboBoxCostCategory.DisplayLayout.ScrollBounds = Infragistics.Win.UltraWinGrid.ScrollBounds.ScrollToFill;
			comboBoxCostCategory.DisplayLayout.ScrollStyle = Infragistics.Win.UltraWinGrid.ScrollStyle.Immediate;
			comboBoxCostCategory.DisplayLayout.ViewStyleBand = Infragistics.Win.UltraWinGrid.ViewStyleBand.OutlookGroupBy;
			comboBoxCostCategory.DropDownSearchMethod = Infragistics.Win.UltraWinGrid.DropDownSearchMethod.Linear;
			comboBoxCostCategory.Editable = true;
			comboBoxCostCategory.FilterString = "";
			comboBoxCostCategory.HasAllAccount = false;
			comboBoxCostCategory.HasCustom = false;
			comboBoxCostCategory.IsDataLoaded = false;
			comboBoxCostCategory.Location = new System.Drawing.Point(274, 2);
			comboBoxCostCategory.MaxDropDownItems = 12;
			comboBoxCostCategory.Name = "comboBoxCostCategory";
			comboBoxCostCategory.ShowInactiveItems = false;
			comboBoxCostCategory.ShowQuickAdd = true;
			comboBoxCostCategory.Size = new System.Drawing.Size(120, 20);
			comboBoxCostCategory.TabIndex = 130;
			comboBoxCostCategory.UseFlatMode = Infragistics.Win.DefaultableBoolean.True;
			base.AutoScaleDimensions = new System.Drawing.SizeF(6f, 13f);
			base.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			BackColor = System.Drawing.Color.WhiteSmoke;
			base.ClientSize = new System.Drawing.Size(656, 513);
			base.Controls.Add(ultraTabControl1);
			base.Controls.Add(panelDetails);
			base.Controls.Add(formManager);
			base.Controls.Add(panelButtons);
			base.Controls.Add(toolStrip1);
			base.Icon = (System.Drawing.Icon)resources.GetObject("$this.Icon");
			base.KeyPreview = true;
			MinimumSize = new System.Drawing.Size(630, 166);
			base.Name = "TTPaymentForm";
			Text = "Bank Transfer Payment Voucher";
			base.FormClosing += new System.Windows.Forms.FormClosingEventHandler(AccountGroupDetailsForm_FormClosing);
			tabPageItems.ResumeLayout(false);
			tabPageItems.PerformLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxBankAccount).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxAnalysis).EndInit();
			tabPageExpense.ResumeLayout(false);
			tabPageExpense.PerformLayout();
			((System.ComponentModel.ISupportInitialize)dataGridExpense).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxGridExpenseCode).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxGridCurrency).EndInit();
			toolStrip1.ResumeLayout(false);
			toolStrip1.PerformLayout();
			panelButtons.ResumeLayout(false);
			panelDetails.ResumeLayout(false);
			panelDetails.PerformLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxSysDoc).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCenter).EndInit();
			((System.ComponentModel.ISupportInitialize)ultraTabControl1).EndInit();
			ultraTabControl1.ResumeLayout(false);
			panelJobCC.ResumeLayout(false);
			panelJobCC.PerformLayout();
			((System.ComponentModel.ISupportInitialize)comboBoxJob).EndInit();
			((System.ComponentModel.ISupportInitialize)comboBoxCostCategory).EndInit();
			ResumeLayout(false);
			PerformLayout();
		}
	}
}
